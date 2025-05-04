import csv

def filter_expenses(file_path):
    print("\n===== FILTER EXPENSES =====")
    
    if not check_file_exists(file_path):
        print("No expenses found. Please add some expenses first.")
        return

    print("Filter by:")
    print("1. Category")
    print("2. Date (YYYY-MM-DD)")
    choice = input("Enter your choice (1 or 2): ").strip()

    if choice == "1":
        category = input("Enter category to filter by: ").strip().lower()
        filter_by_column(file_path, "Category", category)
    elif choice == "2":
        date = input("Enter date to filter by (YYYY-MM-DD): ").strip()
        filter_by_column(file_path, "Date", date)
    else:
        print("Invalid choice. Please enter 1 or 2.")

def check_file_exists(file_path):
    try:
        with open(file_path, 'r') as file:
            return len(file.readlines()) > 1
    except FileNotFoundError:
        return False

def filter_by_column(file_path, column_name, value):
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        filtered = [row for row in reader if row[column_name].strip().lower() == value.lower()]
        
        if filtered:
            print("\nFiltered Expenses:")
            print("{:<12} {:<10} {:<15} {}".format("Date", "Amount", "Category", "Description"))
            print("-" * 55)
            for row in filtered:
                print("{:<12} {:<10} {:<15} {}".format(row['Date'], row['Amount'], row['Category'], row['Description']))
        else:
            print(f"No expenses found for {column_name.lower()} '{value}'.")

if __name__ == "__main__":
    filter_expenses("expenses.csv")
