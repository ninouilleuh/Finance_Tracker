def input_category(message):
    while True:
        try:
            category = input(message)
            if category.strip() == "":
                raise ValueError("Category cannot be empty.")
            return category
        except ValueError as e:
            print(f"Error: {e}")


def input_expense(message):
    while True:
        result = input(message)
        if result.strip() == "" :
                print("Expense amount cannot be empty.")
                continue        
        try:
            result = float(result)
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
            continue

        if result < 0:
            print("Expense amount cannot be negative.")
            continue
        return result
     

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
    
expenses = readfile("expenses.txt")

print("=== Previous Expenses ===")

for expense in expenses:
    print(expense.strip())

print("=========================")

category = input_category("Category: ")
amount = input_expense("Amount: ")

with open("expenses.txt", "a") as file:
    file.write(f"{category} - {amount}\n")