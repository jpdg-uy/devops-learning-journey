# Conventional Commits & PR Workflow Cheatsheet

## Conventional Commits

### Format
```
<prefix>: <short description in imperative tense>
```

### Prefixes

| Prefix | Use for | Example |
|--------|---------|---------|
| `feat:` | New feature or capability | `feat: add health check endpoint` |
| `fix:` | Bug fix | `fix: bind Flask to 0.0.0.0 for WSL2` |
| `docs:` | Documentation changes | `docs: add README to week-3 folder` |
| `chore:` | Maintenance, config, tooling | `chore: add .gitignore to repository` |
| `refactor:` | Restructure without behavior change | `refactor: split nginx config into blocks` |
| `test:` | Adding or updating tests | `test: add unit tests for app routes` |
| `ci:` | CI/CD pipeline changes | `ci: add GitHub Actions workflow` |

### Rules
- Use **imperative tense** — `add`, not `added` or `adding`
- Keep the description **under 72 characters**
- No period at the end
- Lowercase after the colon

---

## PR Description Template

```
## What
Brief description of what changed.

## Why
The problem this solves or the reason for the change.

## Notes
Anything a reviewer should know (config dependencies, quirks, etc.)
```

---

## Branch → PR → Merge Cycle

```bash
# 1. Create feature branch
git checkout -b feature/short-description

# 2. Make changes, then stage and commit
git add .
git commit -m "prefix: description"

# 3. Push branch to remote
git push -u origin feature/short-description

# 4. Open PR on GitHub, write description, merge

# 5. Pull merged main and clean up
git checkout main
git pull
git branch -d feature/short-description
```
