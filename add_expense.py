import csv
from datetime import datetime

def add_expense(file_path):
    """Add a new expense to the CSV file"""
    print("\n===== ADD EXPENSE =====")
    
    # Get expense details from user
    date_input = input("Enter date (YYYY-MM-DD) or press Enter for today: ")
    
    # Use current date if not provided
    if date_input.strip() == "":
        date = datetime.now().strftime("%Y-%m-%d")
    else:
        try:
            # Validate date format
            datetime.strptime(date_input, "%Y-%m-%d")
            date = date_input
        except ValueError:
            print("Invalid date format. Using today's date.")
            date = datetime.now().strftime("%Y-%m-%d")
    
    # Get amount with validation
    while True:
        amount_input = input("Enter amount: ")
        try:
            amount = float(amount_input)
            if amount < 0:
                print("Amount cannot be negative.")
            else:
                break
        except ValueError:
            print("Please enter a valid number.")
    
    # Get category and description
    category = input("Enter category (e.g., Food, Transport, Utilities): ")
    description = input("Enter description (optional): ")
    
    # Check if file exists and create with headers if it doesn't
    try:
        with open(file_path, 'r') as file:
            pass  # File exists do nothing
    except FileNotFoundError:
        with open(file_path, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Amount", "Category", "Description"])
    
    # Save to file
    with open(file_path, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, amount, category, description])
    
    print(f"Expense of {amount} added successfully!")

if __name__ == "__main__":
    # For testing this module independently
    add_expense("expenses.csv")