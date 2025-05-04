#reading from csv
def read_expenses(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()
    return lines

#writing to csv
def write_expenses(file_path, lines):
    with open(file_path, 'w') as f:
        f.writelines(lines)

#deleting the expense continuously
def delete_expense():
    file_path = "expenses.csv"
    
    while True:
        expenses = read_expenses(file_path)
        if not expenses:
            print("No expenses to delete. All cleared!")
            break

        # Show all expenses with numbers
        print("\nExpenses:")
        for idx, expense in enumerate(expenses, start=1):
            print(f"{idx}. {expense.strip()}")

        try:
            choice = int(input("Enter the index number of the expense to delete: "))
            if 1 <= choice <= len(expenses):
                deleted = expenses.pop(choice - 1)
                write_expenses(file_path, expenses)
                print(f"Deleted: {deleted.strip()}")
            else:
                print(f"Invalid number! Please enter a number between 1 and {len(expenses)}.")
        except ValueError:
            print("Please enter a valid index number.")
            continue

        # Keep asking until user enters valid input: y or n
        while True:
            again = input("Do you want to delete another expense? (y/n): ").strip().lower()
            if again == 'y':
                break
            elif again == 'n':
                print("Exiting expense deletion.")
                return
            else:
                print("Invalid input! Please enter 'y' or 'n'.")

if __name__ == "__main__":
    delete_expense()
