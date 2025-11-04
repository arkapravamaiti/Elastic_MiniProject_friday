# Git Workflow Guide - Branch Strategy

## 📌 Branch Setup Complete! ✅

Your repository now has three branches set up following the industry-standard branching strategy:

- **`dev`** - Development branch (for active development)
- **`stage`** - Staging branch (for testing before production)
- **`main`** - Production branch (stable, production-ready code)

## 🌳 Current Repository Structure

```
Elastic_MiniProject_friday/
├── .gitignore
├── README.md
├── requirements.txt
├── it_asset_inventory_cleaned.csv
├── screenshots/
│   ├── Screenshot 2025-11-03 181128.png
│   ├── Screenshot 2025-11-03 181145.png
│   ├── Screenshot 2025-11-03 181308.png
│   └── Screenshot 2025-11-03 181459.png
└── src/
    ├── .env.sample
    ├── .gitattributes
    ├── Readme.md
    ├── main.py
    ├── utils.py
    └── verify_es.py
```

## 🔄 Workflow: dev → stage → main

### Step 1: Development in `dev` Branch

```bash
# Switch to dev branch
git checkout dev

# Make your changes to the code
# ... edit files ...

# Stage and commit changes
git add .
git commit -m "feat: Add new feature description"

# Push to remote dev branch
git push origin dev
```

### Step 2: Create Pull Request from `dev` to `stage`

**Via GitHub Web Interface:**

1. Go to: https://github.com/arkapravamaiti/Elastic_MiniProject_friday
2. Click on "Pull requests" tab
3. Click "New pull request"
4. Set:
   - **Base:** `stage`
   - **Compare:** `dev`
5. Click "Create pull request"
6. Add description and click "Create pull request"
7. Review changes and click "Merge pull request"
8. Confirm merge

**Via Command Line (Alternative):**

```bash
# Switch to stage branch
git checkout stage

# Merge dev into stage
git merge dev

# Push to remote stage
git push origin stage
```

### Step 3: Testing in `stage` Branch

```bash
# Switch to stage branch
git checkout stage

# Pull latest changes
git pull origin stage

# Test the application thoroughly
python src/main.py
python src/verify_es.py

# If issues found, switch back to dev and fix them
```

### Step 4: Create Pull Request from `stage` to `main`

**Via GitHub Web Interface:**

1. Go to: https://github.com/arkapravamaiti/Elastic_MiniProject_friday
2. Click on "Pull requests" tab
3. Click "New pull request"
4. Set:
   - **Base:** `main`
   - **Compare:** `stage`
5. Click "Create pull request"
6. Add description: "Release v1.0 - Production deployment"
7. Click "Create pull request"
8. Review changes carefully
9. Click "Merge pull request"
10. Confirm merge

**Via Command Line (Alternative):**

```bash
# Switch to main branch
git checkout main

# Merge stage into main
git merge stage

# Tag the release (optional but recommended)
git tag -a v1.0 -m "Release version 1.0"

# Push to remote main with tags
git push origin main --tags
```

## 📋 Quick Command Reference

### Branch Operations

```bash
# List all branches
git branch -a

# Switch to a branch
git checkout <branch-name>

# Create and switch to new branch
git checkout -b <new-branch-name>

# Delete a local branch
git branch -d <branch-name>
```

### Checking Status

```bash
# View current status
git status

# View commit history
git log --oneline --graph --all

# View differences
git diff
```

### Syncing with Remote

```bash
# Fetch latest from remote
git fetch origin

# Pull latest changes
git pull origin <branch-name>

# Push changes
git push origin <branch-name>
```

## 🎯 Best Practices

### 1. **Commit Messages**
Use clear, descriptive commit messages:
```
feat: Add new feature
fix: Fix bug in data processing
docs: Update README documentation
refactor: Improve code structure
test: Add unit tests
```

### 2. **Regular Commits**
- Commit often with small, logical changes
- Each commit should represent a single, complete change

### 3. **Pull Before Push**
Always pull the latest changes before pushing:
```bash
git pull origin dev
git push origin dev
```

### 4. **Branch Protection** (Recommended)
Set up branch protection rules on GitHub for `main` and `stage`:
1. Go to repository Settings → Branches
2. Add rule for `main` and `stage`
3. Enable "Require pull request reviews before merging"
4. Enable "Require status checks to pass before merging"

### 5. **Code Review**
- Always create pull requests for merging
- Request code review from team members
- Address feedback before merging

## 🔗 GitHub Repository Links

- **Repository:** https://github.com/arkapravamaiti/Elastic_MiniProject_friday
- **Dev Branch:** https://github.com/arkapravamaiti/Elastic_MiniProject_friday/tree/dev
- **Stage Branch:** https://github.com/arkapravamaiti/Elastic_MiniProject_friday/tree/stage
- **Main Branch:** https://github.com/arkapravamaiti/Elastic_MiniProject_friday/tree/main

## 🚀 Next Steps

1. ✅ Repository cleaned and restructured
2. ✅ Three branches created (dev, stage, main)
3. ✅ Initial code pushed to all branches
4. ⏭️ Start development in `dev` branch
5. ⏭️ Create PR: `dev` → `stage` after testing
6. ⏭️ Create PR: `stage` → `main` after validation

## 📞 Support

For issues or questions:
- Check the [README.md](README.md) for project documentation
- Review commit history: `git log`
- Check branch status: `git status`

---

**Happy Coding! 🎉**
