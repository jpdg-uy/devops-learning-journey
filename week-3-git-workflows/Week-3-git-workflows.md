# Week 3: Git Workflows for DevOps

**Phase:** 1 — Foundations  
**Duration:** 5 days (~1–2 hrs/day)  
**Deliverable:** Flask + Nginx project in a clean, portfolio-ready GitHub repo

---

## Why This Week Matters

In distributed teams, Git is the communication layer. Your commit history, branching strategy, and PR discipline tell colleagues and hiring managers how you work. CI/CD pipelines also trigger off Git events — understanding Git workflows shapes everything in Phase 6 (CI/CD pipelines).

---

## Days 1–2: Branching Strategy & Trunk-Based Development

### Concept

The industry has largely converged on **trunk-based development** for DevOps shops: short-lived branches, frequent merges to `main`, no long-running feature branches.

```
main (production-ready at all times)
  └── feature/add-nginx-config   ← lives 1–2 days max
  └── fix/systemd-service-crash  ← lives hours
```

### Lab

Take the Flask app deployed in Week 2. Practice the full cycle:

```bash
git checkout -b feature/clean-repo-structure
# make changes
git add .
git commit -m "chore: organize project structure for production"
git checkout main
git merge feature/clean-repo-structure
git branch -d feature/clean-repo-structure
```

Repeat this cycle at least 3 times with meaningful changes.

---

## Days 3–4: Commit Discipline & Pull Request Workflow

### Concept

Commits are async communication. Your commit messages should read like a changelog a teammate can scan at 2am during an incident.

**Bad:** `fix stuff`  
**Good:** `fix: bind Flask to 0.0.0.0 for WSL2 compatibility`

**Adopt Conventional Commits:**

| Prefix | Use for |
|--------|---------|
| `feat:` | New feature or capability |
| `fix:` | Bug fix |
| `docs:` | Documentation changes |
| `chore:` | Maintenance, config, tooling |
| `refactor:` | Code restructure without behavior change |

This format is what CI tools parse automatically later in the curriculum.

### PR Discipline (Even When Working Solo)

Write PR descriptions as if a remote colleague who wasn't in your head needs to review it. Practice now so it's habitual when it matters.

**PR description template:**
```
## What
Brief description of what changed.

## Why
The problem this solves or the reason for the change.

## Notes
Anything a reviewer should know (WSL2 quirks, config dependencies, etc.)
```

### Lab

Make 3 meaningful changes to your Flask project using proper Conventional Commits. For each, write a PR description using the template above — even if you're merging it yourself.

---

## Day 5: Git for Operations Work

### Key Commands

```bash
# Visualize history
git log --oneline --graph --all

# Save work-in-progress cleanly
git stash
git stash pop

# Tag a release
git tag -a v1.0.0 -m "Initial production deploy"
git push origin v1.0.0

# Clean up remote-tracking branches
git fetch --prune

# Amend the last commit (before pushing)
git commit --amend --no-edit
```

### Rebase vs Merge

| Scenario | Use |
|----------|-----|
| Cleaning up local commits before a PR | `git rebase -i main` |
| Integrating a finished branch into main | `git merge` |
| Never rebase branches others are using | — |

### `.gitignore` Discipline

A clean `.gitignore` before first commit — never commit secrets, build artifacts, or environment files.

```gitignore
# Python
__pycache__/
*.pyc
*.pyo
venv/
.env
*.egg-info/

# Editor
.vscode/
*.swp

# OS
.DS_Store
Thumbs.db
```

### Lab

1. Run `git log --oneline --graph --all` and read the history
2. Audit your `.gitignore` — add anything missing
3. Tag your current working state: `git tag -a v1.0.0 -m "Week 2 deployment complete"`

---

## Week 3 Deliverable

Your Flask + Nginx deployment from Week 2 lives in a clean, public GitHub repo with:

- [ ] Proper `.gitignore` (no `__pycache__`, `.env`, `venv/`)
- [ ] `README.md` written as a runbook — what it is, how to deploy it, WSL2 notes
- [ ] Meaningful commit history using Conventional Commits (not `first commit` → `fix`)
- [ ] At least one branch → PR description → merge cycle visible in history
- [ ] `v1.0.0` tag on the working state

> **Documentation standard:** The README should assume the reader has never seen this codebase and won't ask questions. Capture *why something didn't work* alongside *what fixed it* — this is what separates a senior DevOps runbook from a junior's.

---

## Progress Tracker

```
Topic: Week 3 — Git Workflows for DevOps
Completion Date:
Key Takeaway:
Blockers Hit:
Next Action:
```

---

## What's Next

**Week 4** begins Phase 2: Containerization. You'll take the Flask app you've just documented and Dockerize it — building on the clean repo structure you've established this week.# Week 3: Git Workflows for DevOps

**Phase:** 1 — Foundations  
**Duration:** 5 days (~1–2 hrs/day)  
**Deliverable:** Flask + Nginx project in a clean, portfolio-ready GitHub repo

---

## Why This Week Matters

In distributed teams, Git is the communication layer. Your commit history, branching strategy, and PR discipline tell colleagues and hiring managers how you work. CI/CD pipelines also trigger off Git events — understanding Git workflows shapes everything in Phase 6 (CI/CD pipelines).

---

## Days 1–2: Branching Strategy & Trunk-Based Development

### Concept

The industry has largely converged on **trunk-based development** for DevOps shops: short-lived branches, frequent merges to `main`, no long-running feature branches.

```
main (production-ready at all times)
  └── feature/add-nginx-config   ← lives 1–2 days max
  └── fix/systemd-service-crash  ← lives hours
```

### Lab

Take the Flask app deployed in Week 2. Practice the full cycle:

```bash
git checkout -b feature/clean-repo-structure
# make changes
git add .
git commit -m "chore: organize project structure for production"
git checkout main
git merge feature/clean-repo-structure
git branch -d feature/clean-repo-structure
```

Repeat this cycle at least 3 times with meaningful changes.

---

## Days 3–4: Commit Discipline & Pull Request Workflow

### Concept

Commits are async communication. Your commit messages should read like a changelog a teammate can scan at 2am during an incident.

**Bad:** `fix stuff`  
**Good:** `fix: bind Flask to 0.0.0.0 for WSL2 compatibility`

**Adopt Conventional Commits:**

| Prefix | Use for |
|--------|---------|
| `feat:` | New feature or capability |
| `fix:` | Bug fix |
| `docs:` | Documentation changes |
| `chore:` | Maintenance, config, tooling |
| `refactor:` | Code restructure without behavior change |

This format is what CI tools parse automatically later in the curriculum.

### PR Discipline (Even When Working Solo)

Write PR descriptions as if a remote colleague who wasn't in your head needs to review it. Practice now so it's habitual when it matters.

**PR description template:**
```
## What
Brief description of what changed.

## Why
The problem this solves or the reason for the change.

## Notes
Anything a reviewer should know (WSL2 quirks, config dependencies, etc.)
```

### Lab

Make 3 meaningful changes to your Flask project using proper Conventional Commits. For each, write a PR description using the template above — even if you're merging it yourself.

---

## Day 5: Git for Operations Work

### Key Commands

```bash
# Visualize history
git log --oneline --graph --all

# Save work-in-progress cleanly
git stash
git stash pop

# Tag a release
git tag -a v1.0.0 -m "Initial production deploy"
git push origin v1.0.0

# Clean up remote-tracking branches
git fetch --prune

# Amend the last commit (before pushing)
git commit --amend --no-edit
```

### Rebase vs Merge

| Scenario | Use |
|----------|-----|
| Cleaning up local commits before a PR | `git rebase -i main` |
| Integrating a finished branch into main | `git merge` |
| Never rebase branches others are using | — |

### `.gitignore` Discipline

A clean `.gitignore` before first commit — never commit secrets, build artifacts, or environment files.

```gitignore
# Python
__pycache__/
*.pyc
*.pyo
venv/
.env
*.egg-info/

# Editor
.vscode/
*.swp

# OS
.DS_Store
Thumbs.db
```

### Lab

1. Run `git log --oneline --graph --all` and read the history
2. Audit your `.gitignore` — add anything missing
3. Tag your current working state: `git tag -a v1.0.0 -m "Week 2 deployment complete"`

---

## Week 3 Deliverable

Your Flask + Nginx deployment from Week 2 lives in a clean, public GitHub repo with:

- [ ] Proper `.gitignore` (no `__pycache__`, `.env`, `venv/`)
- [ ] `README.md` written as a runbook — what it is, how to deploy it, WSL2 notes
- [ ] Meaningful commit history using Conventional Commits (not `first commit` → `fix`)
- [ ] At least one branch → PR description → merge cycle visible in history
- [ ] `v1.0.0` tag on the working state

> **Documentation standard:** The README should assume the reader has never seen this codebase and won't ask questions. Capture *why something didn't work* alongside *what fixed it* — this is what separates a senior DevOps runbook from a junior's.

---

## Progress Tracker

```
Topic: Week 3 — Git Workflows for DevOps
Completion Date:
Key Takeaway:
Blockers Hit:
Next Action:
```

---

## What's Next

**Week 4** begins Phase 2: Containerization. You'll take the Flask app you've just documented and Dockerize it — building on the clean repo structure you've established this week.
