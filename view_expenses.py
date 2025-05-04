import csv
from datetime import datetime
from tabulate import tabulate
#View all expenses sorted by most recent date
def view_expenses(file_path): 
    print("\n===== VIEW ALL EXPENSES =====")
    try:
        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)
            expenses = list(reader)

            if not expenses:
                print("No expenses found.")
                return
            
            # Convert date string to datetime object for sorting
            for expense in expenses:
                expense['Date'] = datetime.strptime(expense['Date'], "%Y-%m-%d") #Parsing the 'Date' from string to time

            # Sort expenses by date descending
            expenses.sort(key=lambda x: x['Date'], reverse=True)  #implies, for each expense x, look for the 'Date' value of x for applying sorting

            # Convert date back to string for display
            for expense in expenses:
                expense['Date'] = expense['Date'].strftime("%Y-%m-%d")

            # Display in table format
            print(tabulate(expenses, headers="keys", tablefmt="grid"))
    
    except FileNotFoundError:
        print("No expense file found. Please add expenses first.")

if __name__ == "__main__":
    # For testing this module independently
    view_expenses("expenses.csv")
