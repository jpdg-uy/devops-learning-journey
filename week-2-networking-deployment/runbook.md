# Runbook: Flask + Nginx Deployment on WSL2

## Section 1: Overview

This runbook describes the steps needed to setup and deploy a Python application on Ubuntu Linux. The final product is a Flask application running as a system service, and an Nginx server as a reverse proxy managing user requests, accessible at `http://myapp.local`.

---

## Section 2: Architecture

We will be running a two layer stack. On the edge, Nginx works as the request manager, listening on port 80 and forwarding to the Flask app running internally on port 5000. The browser request is resolved via a hosts file entry, down through WSL2's forwarding into Nginx, and finally reaches Flask.

```
Browser → hosts file (myapp.local → 127.0.0.1) → WSL2 forwarding → Nginx :80 → Flask :5000
```

---

## Section 3: Prerequisites

A Windows 11 machine with administrator access is required. WSL2 must be installed and configured with an Ubuntu 22.04 distribution running before proceeding.

**Required packages (install via apt):**
```bash
sudo apt update && sudo apt upgrade -y
sudo apt install -y python3 python3-venv python3-pip build-essential nginx
```

---

## Section 4: Application Setup

A dedicated system user is created to encapsulate permissions for the app. In case of a breach, the minimum permission policy contains the damage to the application directory only.

```bash
# Create system user with no home directory and no login shell
sudo useradd --system --no-create-home --shell /usr/sbin/nologin webapp

# Create application directory
sudo mkdir /opt/webapp

# Assign ownership to webapp user
sudo chown webapp:webapp /opt/webapp

# Restrict directory permissions
sudo chmod 750 /opt/webapp

# Create virtual environment as webapp user
sudo -u webapp bash -c "python3 -m venv /opt/webapp/venv"

# Install Flask into the virtual environment
sudo -u webapp bash -c "/opt/webapp/venv/bin/pip install flask"
```

Copy your `app.py` into `/opt/webapp/`.

---

## Section 5: Systemd Service

Create the systemd service file:

```bash
sudo nano /etc/systemd/system/webapp.service
```

Paste the following:

```ini
[Unit]
Description=Flask Web Application
After=network.target        # Wait for network before starting

[Service]
Type=simple
User=webapp                 # Run as non-privileged user
WorkingDirectory=/opt/webapp
ExecStart=/opt/webapp/venv/bin/python3 /opt/webapp/app.py
Restart=always              # Restart automatically on crash

[Install]
WantedBy=multi-user.target  # Start on normal system boot
```

Enable and start the service:

```bash
# Enable on boot
sudo systemctl enable webapp

# Start now
sudo systemctl start webapp

# Verify Flask is running
curl http://127.0.0.1:5000
```

---

## Section 6: Nginx Configuration

Create the Nginx configuration:

```bash
sudo nano /etc/nginx/sites-available/myapp
```

Paste the following:

```nginx
server {
    listen 80;
    listen [::]:80;         # IPv6 equivalent of 0.0.0.0
    server_name myapp.local;

    location / {
        proxy_set_header Host $host;                    # Preserve original hostname
        proxy_set_header X-Real-IP $remote_addr;        # Log real client IP
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;  # Preserve IP chain through proxies
        proxy_pass http://127.0.0.1:5000;               # Forward to Flask
    }
}
```

Enable the site and reload Nginx:

```bash
# Test configuration syntax before applying
sudo nginx -t

# Create symlink to enable site
sudo ln -s /etc/nginx/sites-available/myapp /etc/nginx/sites-enabled/myapp

# Enable on boot
sudo systemctl enable nginx

# Reload to apply new config
sudo systemctl reload nginx
```

---

## Section 7: Hosts File Configuration

Two hosts file entries are required — one in WSL2 and one in Windows.

**WSL2** (`/etc/hosts`):
```
127.0.0.1   myapp.local
```

**Windows** (`C:\Windows\System32\drivers\etc\hosts`) — open as Administrator:
```
127.0.0.1   myapp.local
```

---

## Section 8: Verification

```bash
# Verify Flask is running and responding
curl http://127.0.0.1:5000

# Verify full stack through Nginx
curl http://myapp.local

# Check service status
sudo systemctl status webapp
sudo systemctl status nginx
```

Expected: HTML response from your Flask app on both commands.

---

## Section 9: Troubleshooting

**Check logs:**
```bash
# Flask application logs
sudo journalctl -u webapp -f

# Nginx error log
sudo tail -f /var/log/nginx/error.log

# Nginx access log
sudo tail -f /var/log/nginx/access.log
```

**Common issues:**
- Nginx config error → run `sudo nginx -t` to identify the problem
- Flask not responding → run `sudo systemctl status webapp` and check logs
- Can't reach from browser → verify Windows hosts file entry

---

## Section 10: Updating the Application

When `app.py` changes, only the Flask service needs to restart — Nginx config is unchanged:

```bash
# Copy updated app.py to /opt/webapp/
sudo cp app.py /opt/webapp/app.py
sudo chown webapp:webapp /opt/webapp/app.py

# Restart Flask service
sudo systemctl restart webapp

# Verify it came back up
sudo systemctl status webapp
```
