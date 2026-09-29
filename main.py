"""
Simple Expense Tracker
-----------------------
Concepts used: functions, lists, dictionaries, loops, file handling.
"""

import csv
import os

FILENAME = "expenses.csv"


# Load expenses from the file when the program starts
def load_expenses():
    expenses = []
    if os.path.exists(FILENAME): 
        with open(FILENAME, "r", newline="") as file:
            reader = csv.DictReader(file)
            for row in reader:
                row["amount"] = float(row["amount"])
                expenses.append(row)
    return expenses


# Save all expenses back to the file
def save_expenses(expenses):
    with open(FILENAME, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["category", "amount", "note"])
        writer.writeheader()
        writer.writerows(expenses)


# Add a new expense
Name=input("Enter your name: ")
print(Name)
date=input("Enter Date in(dd/mm/yy): ")
print(date)
def add_expense(expenses):
    category = input("Enter category (Food/Travel/Shopping/Other): ")
    amount = float(input("Enter amount: "))
    note = input("Enter a short note: ")

    expense = {"category": category, "amount": amount, "note": note}
    expenses.append(expense)
    save_expenses(expenses)
    print("Expense added!\n")


# Show all expenses
def view_expenses(expenses):
    if not expenses:
        print("No expenses yet.\n")
        return

    print("\n--- All Expenses ---")
    for i, e in enumerate(expenses, start=1):
        print(f"{i}. {e['category']} - Rs.{e['amount']} ({e['note']})")
    print()


# Show total spent, grouped by category
def show_totals(expenses):
    if not expenses:
        print("No expenses yet.\n")
        return

    totals = {}
    for e in expenses:
        category = e["category"]
        totals[category] = totals.get(category, 0) + e["amount"]

    print("\n--- Totals by Category ---")
    grand_total = 0
    for category, amount in totals.items():
        print(f"{category}: Rs.{amount}")
        grand_total += amount
    print(f"TOTAL SPENT: Rs.{grand_total}\n")


# Check if spending crossed a budget the user sets
def check_budget(expenses):
    budget = float(input("Enter your monthly budget: "))
    total = sum(e["amount"] for e in expenses)

    print(f"\nYou have spent Rs.{total} out of Rs.{budget}")
    if total > budget:
        print("Warning! You have gone OVER budget.\n")
    elif total > budget * 0.8:
        print("Careful! You have used more than 80% of your budget.\n")
    else:
        print("You are within your budget. Good job!\n")


# Main menu loop
def main():
    expenses = load_expenses()

    while True:
        print("===== EXPENSE TRACKER =====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Show Totals")
        print("4. Check Budget")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            show_totals(expenses)
        elif choice == "4":
            check_budget(expenses)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.\n")


if __name__ == "__main__":
    main()
