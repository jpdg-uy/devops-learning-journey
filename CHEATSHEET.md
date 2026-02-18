# DevOps Learning Journey - Command Cheatsheet

This is a living document tracking commands, concepts, and patterns learned throughout my 26-week DevOps journey.

---

## Week 1: Linux Fundamentals

### File Navigation & Inspection

| Command | Purpose | Example |
|---------|---------|---------|
| `cd <path>` | Change directory | `cd /var/log` |
| `ls -l` | Long listing format | `ls -l /opt/webapp` |
| `ls -lh` | Human-readable sizes | `ls -lh /var/log` |
| `ls -la` | Show hidden files | `ls -la ~` |
| `pwd` | Print working directory | `pwd` |
| `du -sh *` | Disk usage summary | `du -sh * \| sort -h` |
| `tail -n 20 <file>` | View last 20 lines | `tail -n 20 /var/log/syslog` |
| `head -n 10 <file>` | View first 10 lines | `head -n 10 app.log` |
| `cat <file>` | Display entire file | `cat /etc/passwd` |
| `grep <pattern> <file>` | Search for pattern | `grep error app.log` |
| `grep -v <pattern>` | Invert match (exclude) | `ps aux \| grep -v grep` |

### Pipes and Filtering

| Pattern | Purpose | Example |
|---------|---------|---------|
| `cmd1 \| cmd2` | Pipe output to input | `ls -l \| grep "^d"` |
| `cmd \| grep <pattern>` | Filter output | `ps aux \| grep python` |
| `cmd \| grep -v <pattern>` | Exclude pattern | `ps aux \| grep -v grep` |
| `cmd \| column -t -s ':'` | Format output in columns | `cat /etc/passwd \| column -t -s ':'` |

### Permissions & Ownership

**Permission String Format:** `-rwxr-xr-x`
- Position 1: File type (`-` = file, `d` = directory, `l` = symlink)
- Positions 2-4: Owner permissions (read, write, execute)
- Positions 5-7: Group permissions
- Positions 8-10: Others permissions

**Permission Values:**
- `r` (read) = 4
- `w` (write) = 2  
- `x` (execute) = 1

| Command | Purpose | Example |
|---------|---------|---------|
| `chmod +x <file>` | Make file executable | `chmod +x script.sh` |
| `chmod 755 <file>` | rwxr-xr-x | `chmod 755 /opt/webapp/app.py` |
| `chmod 644 <file>` | rw-r--r-- | `chmod 644 config.txt` |
| `chmod 700 <file>` | rwx------ | `chmod 700 private.sh` |
| `chown user:group <file>` | Change ownership | `chown webapp:webapp /opt/webapp` |
| `chown -R user:group <dir>` | Recursive ownership | `chown -R webapp:webapp /opt/webapp` |

**Common Permission Patterns:**
- `755` - Directories, executable scripts (owner: full, others: read/execute)
- `644` - Regular files (owner: read/write, others: read-only)
- `700` - Private directories (owner only)
- `600` - Private files (owner read/write only)

### User & Group Management

| Command | Purpose | Example |
|---------|---------|---------|
| `whoami` | Show current user | `whoami` |
| `id` | Show user ID and groups | `id` |
| `groups` | Show group memberships | `groups` |
| `sudo useradd --system --no-create-home --shell /usr/sbin/nologin <user>` | Create system user | `sudo useradd --system --no-create-home --shell /usr/sbin/nologin webapp` |
| `sudo -u <user> <cmd>` | Run command as user | `sudo -u webapp touch file.txt` |

### Process Management

| Command | Purpose | Example |
|---------|---------|---------|
| `ps aux` | List all processes | `ps aux` |
| `ps -ef` | List processes (alternative format) | `ps -ef` |
| `ps aux \| grep <name>` | Find specific process | `ps aux \| grep python` |
| `kill <PID>` | Terminate process | `kill 1234` |
| `kill -9 <PID>` | Force kill process | `sudo kill -9 1234` |
| `jobs` | List background jobs | `jobs` |
| `bg` | Resume job in background | `bg` |
| `fg` | Bring job to foreground | `fg` |

### Running Processes in Background

| Pattern | Purpose | Example |
|---------|---------|---------|
| `<cmd> &` | Run in background | `python3 app.py &` |
| `nohup <cmd> &` | Background, survives logout | `nohup python3 app.py &` |
| `nohup <cmd> > log 2>&1 &` | Background with logging | `nohup python3 app.py > app.log 2>&1 &` |

**Redirect operators:**
- `>` - Redirect stdout to file
- `2>&1` - Redirect stderr to same place as stdout
- `&` - Run in background

### Package Management (APT)

| Command | Purpose | Example |
|---------|---------|---------|
| `sudo apt update` | Update package lists | `sudo apt update` |
| `sudo apt upgrade` | Upgrade installed packages | `sudo apt upgrade -y` |
| `sudo apt install <pkg>` | Install package | `sudo apt install python3-venv` |
| `apt search <term>` | Search for packages | `apt search flask` |

### Python Virtual Environments

| Command | Purpose | Example |
|---------|---------|---------|
| `python3 -m venv <name>` | Create virtual environment | `python3 -m venv venv` |
| `source venv/bin/activate` | Activate venv | `source venv/bin/activate` |
| `deactivate` | Deactivate venv | `deactivate` |
| `venv/bin/pip install <pkg>` | Install package in venv | `venv/bin/pip install flask` |
| `venv/bin/pip list` | List installed packages | `venv/bin/pip list` |

### systemd Service Management

| Command | Purpose | Example |
|---------|---------|---------|
| `sudo systemctl start <service>` | Start service | `sudo systemctl start webapp` |
| `sudo systemctl stop <service>` | Stop service | `sudo systemctl stop webapp` |
| `sudo systemctl restart <service>` | Restart service | `sudo systemctl restart webapp` |
| `sudo systemctl status <service>` | Check service status | `sudo systemctl status webapp` |
| `sudo systemctl enable <service>` | Auto-start on boot | `sudo systemctl enable webapp` |
| `sudo systemctl disable <service>` | Disable auto-start | `sudo systemctl disable webapp` |
| `sudo systemctl daemon-reload` | Reload service definitions | `sudo systemctl daemon-reload` |
| `sudo journalctl -u <service>` | View service logs | `sudo journalctl -u webapp` |
| `sudo journalctl -u <service> -f` | Follow live logs | `sudo journalctl -u webapp -f` |
| `sudo journalctl -u <service> -n 50` | Last 50 log lines | `sudo journalctl -u webapp -n 50` |

### systemd Service File Structure

Location: `/etc/systemd/system/<service>.service`
```ini
[Unit]
Description=Service description
After=network.target

[Service]
Type=simple
User=serviceuser
WorkingDirectory=/path/to/app
ExecStart=/path/to/command
Restart=always

[Install]
WantedBy=multi-user.target
```

---

## Key Concepts Learned

### Principle of Least Privilege
- Run services as dedicated system users, not root
- Give only the minimum permissions needed
- Limit blast radius if service is compromised

### Permission Hierarchy
Linux checks permissions in order:
1. Are you the owner? → Use owner permissions
2. Are you in the group? → Use group permissions  
3. Neither? → Use others permissions

### Process Lifecycle
- Foreground processes block terminal
- Background processes (`&`) run concurrently but die with terminal
- `nohup` makes processes survive terminal closure
- systemd services are the proper way to run persistent services

---

## Week 1 Project: Flask Web Application

**Deployed:** Python Flask web server  
**User:** `webapp` (system user, no login)  
**Location:** `/opt/webapp/`  
**Service:** `webapp.service` (systemd)  
**Access:** `http://localhost:5000`

**Commands to manage:**
```bash
sudo systemctl status webapp
sudo systemctl restart webapp
sudo journalctl -u webapp -f
curl http://localhost:5000
```

---

*This cheatsheet will be updated weekly as new skills are learned.*
