# 🧠 Habit Tracker CLI

A **Command Line Interface (CLI)** application built in Python to track, complete, and analyze personal habits.  
Developed as part of the **DLBDSOOFPP01** course requirements.

---

## ✅ Key Features

- **Add new habits** — choose between *daily* or *weekly*
- **Mark habits as completed** to track progress
- **Automatic data persistence** — all changes saved to `habits.json`
- **Analyze your habits**:
  - View all tracked habits
  - Filter by periodicity (daily/weekly)
  - Find the **longest streak** across all habits
  - Check the **longest streak for a specific habit**

---

## ▶️ Running the Program

1. Open **Command Prompt (cmd)**.
2. Navigate to the project folder:

```bash
cd C:\Users\admin\Desktop\zohreh\Python\habit_tracker
```

3. Start the program:

```bash
python main.py
```

4. Follow the interactive on-screen menu.

---

## 🧪 Running the Tests

1. Ensure `tests/` contains the file `__init__.py`.
2. Run:

```bash
python -m unittest tests.test_habits
```

Expected output:

```
.......
----------------------------------------------------------------------
Ran 7 tests in 0.001s

OK
```

---

## 📁 Project Structure

```
habit_tracker/
├── analytics.py       # Analysis functions
├── habit.py           # Habit class
├── main.py            # CLI entry point
├── manager.py         # Habit manager class
├── storage.py         # Save/load habits to JSON
├── data/
│   └── habits.json    # Habit data file
├── tests/
│   ├── __init__.py
│   └── test_habits.py # Unit tests
```

---

## 📌 Requirements Fulfilled

✔ Display all habits  
✔ Filter by periodicity  
✔ Find longest global streak  
✔ Find longest streak per habit  
✔ Interactive CLI for user actions  
✔ Automated unit tests with `unittest`

---

© 2025 — Habit Tracker — Developed for the DLBDSOOFPP01 course
