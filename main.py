SEPARATOR = " | "

def input_category(message):
    while True:
        category = input(message)
        if category.strip() == "":
            print("Category cannot be empty.")
            continue
        return category

def readfile(txtfile):
    try:
        with open(txtfile, "r") as file:
            return file.readlines()
    except FileNotFoundError:
        return []

def ask_float(message):
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
    
def statistics(expenses):
    print("===== Statistics =====\n")
    totals = {}
    if expenses == []:
        print("No expenses recorded yet.\n")
        return
    for expense in expenses:
        category, amount = expense.strip().split(SEPARATOR)
        totals[category] = totals.get(category, 0) + float(amount)
    #sort totals categories by total amount spent in descending order
    totals = dict(sorted(totals.items(), key=lambda item: item[1], reverse=True))
    
    for category, total in totals.items():
        print(f"  {category}: {total}")
    print("Total spent: ", sum(float(expense.strip().split(SEPARATOR)[1]) for expense in expenses))
    print("Highest category:")
    if totals:
        highest_category = max(totals, key=totals.get)
        print(f"  {highest_category}")
        print(f"  ${totals[highest_category]}")
    print("=======================")

def previous_expenses(expenses):
    print("=== Previous Expenses ===")

    if expenses == []:
        print("\nNo expenses recorded yet.\n")
    else:
        for expense in expenses:
            print(expense.strip())

    print("=========================")

def new_expense():
    category = input_category("Category: ")
    amount = ask_float("Amount: ")

    with open("expenses.txt", "a") as file:
        file.write(f"{category} | {amount}\n")
    return category, amount

def await_user():
    input("Press Enter to continue...")

def select_option():
    while True:
        print("1. View Statistics")
        print("2. View Previous Expenses")
        print("3. Add New Expense")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice in ["1", "2", "3", "4"]:
            return choice
        else:
            print("Invalid choice. Please try again.")  
def main():
    expenses = readfile("expenses.txt")
    while True:
        choice = select_option()
        if choice == "1":
            statistics(expenses)
            await_user()
        elif choice == "2":
            previous_expenses(expenses)
            await_user()
        elif choice == "3":
            category, amount = new_expense()
            expenses.append(f"{category} | {amount}\n")  # Update the expenses list
        elif choice == "4":
            confirm = input("Are you sure you want to exit? (y/n): ")
            if confirm.lower() == "y":
                break
        else:
            print("Invalid choice. Please try again.")
main()