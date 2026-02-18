# Week 1: Linux Fundamentals & Web Application Deployment

## Completion Date
February 18, 2026

## Time Invested
8 hours across 5 days

## What I Built

### System User
- Created `webapp` system user with no login shell
- User ID: 999
- Home: /home/webapp (not created on disk)
- Shell: /usr/sbin/nologin
- Purpose: Run web application with minimal privileges

### Application Structure
```
/opt/webapp/
├── app.py              # Flask web application
├── venv/               # Python virtual environment
└── app.log            # Application logs (when using nohup)
```

### systemd Service
- Service name: `webapp.service`
- Location: `/etc/systemd/system/webapp.service`
- Auto-starts on boot: Yes
- Restart policy: Always
- Logs: `journalctl -u webapp`

### Access
- URL: http://localhost:5000
- Also accessible from Windows host: http://172.22.14.12:5000

## Key Commands Used

### Service Management
```bash
sudo systemctl start webapp
sudo systemctl stop webapp
sudo systemctl restart webapp
sudo systemctl status webapp
sudo journalctl -u webapp -f
```

### Testing
```bash
curl http://localhost:5000
ps aux | grep python | grep -v grep
```

## Skills Learned

### Day 1: File Navigation
- `ls`, `cd`, `pwd`
- `tail`, `head`, `cat`, `grep`
- `du`, `sort`, pipes

### Day 2: Permissions
- Understanding `rwxr-xr-x` format
- Numeric permissions (755, 644, 700)
- `chmod`, `chown`
- Owner vs group vs others

### Day 3: System Users
- Creating service accounts
- `useradd` with system flags
- Running commands as other users (`sudo -u`)
- Security principle: least privilege

### Day 4: Python Deployment
- Virtual environments (`python3 -m venv`)
- Installing packages (`pip install`)
- Running web applications
- Understanding localhost and port binding

### Day 5: Process Management
- Viewing processes (`ps aux`)
- Background execution (`&`)
- `nohup` for terminal independence
- systemd service creation
- Log viewing with `journalctl`

## Challenges Encountered

### Permission Issues with Output Redirection
**Problem:** `sudo -u webapp command > file` failed because redirection happens in my shell, not as webapp user

**Solution:** Used `sudo -u webapp bash -c 'command > file'` to wrap everything including redirection

### SSH Authentication (Week 0 carryover)
**Problem:** GitHub no longer accepts passwords

**Solution:** Generated SSH key pair, added public key to GitHub, switched remote from HTTPS to SSH

## Key Takeaway

Gained CLI fluency - can now navigate, manage files, understand permissions, and deploy applications without constantly searching for commands. The hands-on trial-and-error approach solidified concepts far better than reading documentation alone.

## Next Steps

Week 2: Networking Fundamentals
- TCP/IP basics
- DNS
- Ports and services
- Firewall concepts
