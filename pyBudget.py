import csv
from datetime import datetime


# Function to set a budget
def set_budget():
    try:
        budget = float(input("Set your monthly budget: $"))
        print(f"Budget set to ${budget:.2f}\n")
        return budget
    except ValueError:
        print("Invalid input. Please enter a valid number for the budget.\n")
        return 0.0


# Function to add an expense
def add_expense(expenses):
    date = input("Enter the date (YYYY-MM-DD): ")
    category = input("Enter the category (e.g., Food, Travel, Bills): ")
    description = input("Enter a description: ")
    try:
        amount = float(input("Enter the amount: $"))
        expenses.append({
            'date': date,
            'category': category,
            'description': description,
            'amount': amount
        })
        print("Expense added successfully!\n")
    except ValueError:
        print("Invalid input. Please enter a valid amount.\n")


# Function to view expenses
def view_expenses(expenses):
    print(f"{'Date':<12}{'Category':<15}{'Description':<30}{'Amount':<10}")
    print('-' * 70)
    for expense in expenses:
        print(f"{expense['date']:<12}{expense['category']:<15}{expense['description']:<30}{expense['amount']:<10.2f}")
    print()


# Function to calculate total expenses
def total_expenses(expenses):
    return sum(expense['amount'] for expense in expenses)


# Function to display total expenses and compare with budget
def budget_status(expenses, budget):
    total = total_expenses(expenses)
    print(f"Total expenses: ${total:.2f}")

    if budget > 0:
        remaining_budget = budget - total
        if remaining_budget > 0:
            print(f"You are within budget. Remaining budget: ${remaining_budget:.2f}\n")
        else:
            print(f"Budget exceeded by: ${-remaining_budget:.2f}\n")
    else:
        print("No budget set yet.\n")


# Function to save expenses to a CSV file
def save_to_csv(expenses, budget, filename='expenses.csv'):
    with open(filename, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['date', 'category', 'description', 'amount'])
        writer.writeheader()
        writer.writerows(expenses)

    # Save budget to a separate file
    with open('budget.csv', mode='w', newline='') as file:
        file.write(str(budget))

    print(f"Expenses and budget saved successfully!\n")


# Function to load expenses from a CSV file
def load_from_csv(filename='expenses.csv'):
    expenses = []
    try:
        with open(filename, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                row['amount'] = float(row['amount'])  # Convert amount back to float
                expenses.append(row)
    except FileNotFoundError:
        print(f"{filename} not found. Starting a new expense list.\n")
    return expenses


# Function to load budget from a CSV file
def load_budget(filename='budget.csv'):
    try:
        with open(filename, mode='r') as file:
            budget = float(file.read())
            print(f"Loaded budget: ${budget:.2f}\n")
            return budget
    except FileNotFoundError:
        print(f"No budget file found. Starting with no budget set.\n")
    except ValueError:
        print(f"Invalid budget data in file. Starting with no budget set.\n")
    return 0.0


# Main program loop
def main():
    expenses = load_from_csv()  # Load expenses from CSV
    budget = load_budget()  # Load budget from CSV

    while True:
        print("Expense Tracker Menu")
        print("1. Set Budget")
        print("2. Add Expense")
        print("3. View Expenses")
        print("4. View Total and Budget Status")
        print("5. Save Expenses and Budget")
        print("6. Exit")
        choice = input("Choose an option (1-6): ")

        if choice == '1':
            budget = set_budget()
        elif choice == '2':
            add_expense(expenses)
        elif choice == '3':
            view_expenses(expenses)
        elif choice == '4':
            budget_status(expenses, budget)
        elif choice == '5':
            save_to_csv(expenses, budget)
        elif choice == '6':
            save_to_csv(expenses, budget)
            print("Exiting the expense tracker.")
            break
        else:
            print("Invalid option. Please try again.\n")


if __name__ == "__main__":
    main()
