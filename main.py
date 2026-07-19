SEPARATOR = " | "
EXPENSES_FILE = "expenses.txt"

def load_expenses():
    try:
        with open(EXPENSES_FILE, "r") as file:
            return file.readlines()
    except FileNotFoundError:
        return []

def input_category(message):
    while True:
        category = input(message)
        if category.strip() == "":
            print("Category cannot be empty.")
            continue
        return category

def input_float(message):
    while True:
        result = input(message)
        if result.strip() == "" :
                print("Input cannot be empty.")
                continue        
        try:
            result = float(result)
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
            continue
        if result < 0:
            print("Input cannot be negative.")
            continue
        return result

def save_expenses(expenses):
    with open(EXPENSES_FILE, "w") as file:
        file.writelines(expenses)
def parse_expense(expense):
    category, amount = expense.strip().split(SEPARATOR)
    return category, float(amount)
  
def statistics(expenses):
    print("===== Statistics =====\n")
    totals = {}
    if not expenses:
        print("No expenses recorded yet.\n")
        return
    for expense in expenses:
        category, amount = parse_expense(expense)
        totals[category] = totals.get(category, 0) + amount
    #sort totals categories by total amount spent in descending order
    totals = dict(sorted(totals.items(), key=lambda item: item[1], reverse=True))
    
    for category, total in totals.items():
        print(f"  {category}: {total}")
    print("Total spent: ", sum(totals.values()))
    print("Highest category:")
    if totals:
        highest_category = max(totals, key=totals.get)
        print(f"  {highest_category}")
        print(f"  ${totals[highest_category]}")
    print("=======================")

def previous_expenses(expenses):
    print("=== Previous Expenses ===")

    if not expenses:
        print("\nNo expenses recorded yet.\n")
    else:
        for expense in expenses:
            print(expense.strip())

    print("=========================")

def new_expense(expenses):
    category = input_category("Category: ")
    amount = input_float("Amount: ")

    expenses.append(f"{category}{SEPARATOR}{amount}\n")
    save_expenses(expenses)
    print("Expense saved.")

def delete_expense(expenses):
    if not expenses:
        print("No expenses to delete.")
        return expenses

    print("=== Expenses ===")
    for index, expense in enumerate(expenses):
        print(f"{index + 1}. {expense.strip()}")

    while True:
        try:
            choice = int(input("Enter the number of the expense to delete (or 0 to cancel): "))
            if choice == 0:
                print("Deletion cancelled.")
                return expenses
            elif 1 <= choice <= len(expenses):
                #ask for confirmation before deleting
                confirm = input(f"Are you sure you want to delete '{expenses[choice - 1].strip()}'? (y/n): ")
                #keep asking for confirmation until the user enters 'y' or 'n'
                while confirm.strip().lower() not in ["y", "n"]:
                    confirm = input("Please enter 'y' or 'n': ")
                if confirm.strip().lower() != "y":
                    print("Deletion cancelled.")
                    return expenses
                deleted_expense = expenses.pop(choice - 1)
                save_expenses(expenses)
                print(f"Deleted expense: {deleted_expense.strip()}")
                return expenses
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def await_user():
    input("Press Enter to continue...")

def select_option():
    while True:
        print("1. View Statistics")
        print("2. View Previous Expenses")
        print("3. Add New Expense")
        print("4. Delete Expense")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice in ["1", "2", "3", "4","5"]:
            return choice
        else:
            print("Invalid choice. Please try again.")  

def main():
    expenses = load_expenses()
    while True:
        choice = select_option()
        if choice == "1":
            statistics(expenses)
            await_user()
        elif choice == "2":
            previous_expenses(expenses)
            await_user()
        elif choice == "3":
            new_expense(expenses)
        elif choice == "4":
            delete_expense(expenses)
        elif choice == "5":
            confirm = input("Are you sure you want to exit? (y/n): ")
            if confirm.strip().lower() == "y":
                break
        else:
            print("Invalid choice. Please try again.")

main()