# 🧰 Git Basic Commands Cheat Sheet

## 📌 Setup (One-time)

```bash
git config --global user.name "Your Name"
git config --global user.email "your-email@example.com"
```

---

## 📁 Initialize Project

```bash
git init
```

---

## ➕ Add Files

```bash
git add .          # add all files
git add filename   # add specific file
```

---

## 💾 Commit Changes

```bash
git commit -m "Your message"
```

---

## 🔍 Check Status

```bash
git status
```

---

## 🌿 Branches

```bash
git branch                 # list branches
git branch -M main         # rename to main
git checkout -b feature    # create new branch
git checkout main          # switch branch
```

---

## 🔗 Connect to GitHub

```bash
git remote add origin https://github.com/USERNAME/REPO.git
git remote -v
```

---

## 🚀 Push to GitHub

```bash
git push -u origin main
```

---

## ⬇️ Pull from GitHub

```bash
git pull origin main
```

---

## 🔄 Rebase (clean history)

```bash
git pull origin main --rebase
```

---

## ⚠️ Force Push (use carefully)

```bash
git push -f origin main
```

---

## 🧹 Undo Changes

### Unstage file:

```bash
git reset filename
```

### Discard changes:

```bash
git checkout -- filename
```

---

## 📜 View History

```bash
git log
git log --oneline
```

---

## 💡 Tips

* Commit often with clear messages
* Never use `-f` unless you understand the impact
* Keep your repo clean with `.gitignore`
* Always pull before push in team environments

---

## 👨‍💻 Your Workflow

```bash
git add .
git commit -m "Describe your change"
git push
```
