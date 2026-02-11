# Week 0: Environment Stup
## Date: 11-FRB-2026

## System info:
- OS: [Ubuntu 22.04.5LTS]
- WSL Version : WSL version: 2.5.10.0

## Installation Steps
1. Updated package lists: 'sudo apt update'
2. Upgraded packages: 'sudo apt upgrade -y'
3. Installed tools: git, curl, wget, vim, build-essentials

## Git Configuration
- Name: Juan Pablo
- Email: juan.pablo.digiovanni@gmail.co

## Authentication issue and resolution
 - **Problem**: Git push failed with "Password authentication is not supported"
- **Root Cause**: GitHub requires SSH keys or Personal Access Tokens, not passwords
- **Solution**: Generated SSH key pair, added public key to GitHub, switched remote from HTTPS to SSH
- **Commands Used**:
  - `ssh-keygen -t ed25519 -C "email@example.com"`
  - `cat ~/.ssh/id_ed25519.pub` (to view public key)
  - `git remote remove origin`
  - `git remote add origin git@github.com:jpdg-uy/devops-learning-journey.git`
  - `ssh -T git@github.com` (to test connection)

