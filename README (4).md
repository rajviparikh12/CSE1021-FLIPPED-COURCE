# Simple Expense Tracker

## Overview
A beginner-friendly command-line program for tracking daily expenses. Users can log an expense with a category, amount, and short note; the program saves everything to a CSV file so nothing is lost between runs, and can show all expenses, totals by category, and whether spending has crossed a user-set monthly budget.

## Features
- **Add Expense** — record a category (Food/Travel/Shopping/Other), an amount, and a short note for each expense.
- **View Expenses** — list every expense logged so far, numbered in order.
- **Show Totals** — group and sum spending by category, plus a grand total.
- **Check Budget** — enter a monthly budget and see how much has been spent against it, with a warning if you've gone over budget or used more than 80% of it.
- **Persistent storage** — expenses are saved to `expenses.csv` and reloaded automatically the next time the program runs.
- **Simple menu loop** — a numbered menu (1–5) drives all the above, with input validation for invalid choices.

## Technologies / Tools Used
- Python 3
- `csv` module (reading/writing `expenses.csv`)
- `os` module (checking whether the data file already exists)
- Core concepts: functions, lists, dictionaries, loops, file handling

## Steps to Install & Run
1. Make sure Python 3 is installed (`python3 --version` to check). No third-party packages are required.
2. Save the script as `simple_expense_tracker.py`.
3. Open a terminal in that folder and run:
   ```bash
   python3 simple_expense_tracker.py
   ```
4. Follow the on-screen menu (options 1–5). An `expenses.csv` file will be created automatically in the same folder the first time you add an expense.

## Instructions for Testing
1. **Add expenses** (option 1) — add a few expenses across different categories (e.g. Food, Travel, Shopping) with different amounts and notes.
2. **View expenses** (option 2) — confirm every expense you added appears, in order, with the correct category, amount, and note.
3. **Show totals** (option 3) — confirm each category's total is the correct sum of its expenses, and that the grand total matches the sum of everything added.
4. **Check budget** (option 4) — test three cases:
   - A budget higher than total spending → should show "within your budget."
   - A budget where spending is over 80% of it but not over → should show the "Careful!" warning.
   - A budget lower than total spending → should show the "over budget" warning.
5. **Empty state** — delete or rename `expenses.csv` and run the program fresh; options 2 and 3 should report "No expenses yet." instead of erroring.
6. **Persistence** — close and reopen the program; expenses added in an earlier run should still be there.
7. **Invalid menu input** — enter a number outside 1–5 (or a letter) at the main menu; the program should print "Invalid choice, try again." and re-show the menu instead of crashing.
8. **Exit** — option 5 should print "Goodbye!" and close the program.

## Screenshots
A full sample run — adding three expenses, viewing them, showing totals, and checking a budget (triggering the "Careful!" warning at 97.5% used):

![Simple Expense Tracker terminal session](screenshot.png)
