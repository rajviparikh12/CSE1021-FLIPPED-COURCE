# Simple Expense Tracker
How it works and what it outputs
## 1. What This Project Does
This is a command-line (text-based) program that helps you track your daily expenses. 
You can add an expense, view all of them, see totals grouped by category, and check whether you are within a budget. 
All data is saved to a file called expenses.csv, so nothing is lost when you close the program.
## Concepts used:
* Variables — to store category, amount, note, etc.
* Lists — to store all expenses together, one after another.
* Dictionaries — to store one expense as key-value pairs.
* Functions — one function per task (add, view, totals, budget).
* Loops — to repeat the menu, and to go through the expense list
* File handling — to save and load data using a CSV file.
* if / elif / else — to decide what the menu option does.
## 2.How the Program Runs (Step by Step) :
* The program starts and calls load_expenses(). This checks if expenses.csv already exists.
If yes, it reads old data into a list. If not, the list starts empty: []
* A while True loop shows the menu again and again until you choose Exit.
* Whatever number you type (1 to 5) decides which function runs next, using if / elif statements
* Every time you add an expense, it is immediately saved to the CSV file — so even if the program crashes, your data up to that point is safe.
 ## The Menu
 ===== EXPENSE TRACKER ===== 
 1. Add Expense
 2. View Expenses
 3. Show Totals
 4. Check Budget
 5. Exit Choose an option (1-5):
## 3. Each Menu Option Explained
* Option 1 — Add Expense
  Asks for a category, amount, and note. These three values are stored together in a dictionary, like a labelled box:
  expense = {"category": "Food", "amount": 150.0, "note": "Lunch with friends"}
  This dictionary is then added to the expenses list using expenses.append(expense), and the whole list is saved to the CSV file.
  Sample run:
        Enter category (Food/Travel/Shopping/Other):
        Food Enter amount: 150
        Enter a short note: Lunch with friends
        Expense added!
  * Option 2 — View Expenses
    Goes through the list one by one using a for loop and enumerate(), which gives both the position number and the expense itself.
    --- All Expenses --
    1. Food - Rs.150.0 (Lunch with friends)
    2. Travel - Rs.60.0 (Bus fare)
  * Option 3 — Show Totals
    Builds a new dictionary called totals where each category name is a key, and the value is the sum of all amounts in that category:
    
    * Option 4 — Check Budget
      Asks for your budget, adds up every expense, and compares the two numbers with simple if / elif / else

    * Option 5 — Exit
      Prints "Goodbye!" and uses break to stop the while True loop, ending the program.
    ## Where Your Data Is Stored
         Every expense is saved as one row in a file named expenses.csv, sitting in the same folder as the program. You can open this file directly in Excel or Notepad.
    ## 5. How to Run This Program
    * Save the file as simple_expense_tracker.py
    * No extra libraries needed — only Python's built-in csv and os modules are used.
    * Open a terminal in the same folder
    * Type: python simple_expense_tracker.py
    
 
