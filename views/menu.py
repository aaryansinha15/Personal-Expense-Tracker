from utils.file_operation_file import read, write
from utils.validation_file import validate_file
from utils.summmary import calculate_total_expenses,calculate_category_summary


EXPENSE_FILE="data\\expenses.json"
CATEGORIES_FILE="data\\categories.json"


def display_menu():
    print("\n-- Personal Expense Tracker---")
    print("1. Add Expenses")
    print("2. View Expenses")
    print("3.View Summary")
    print("4. Move Out")

# user input to select the choice
    choice= input("Enter your choice")

    if choice == 1:
        expense_add()
    elif choice == 2:
        expense_view()
    elif choice == 3:
        expense_summary()
    elif choice == 4:
        print("See you again")
        exit()
    else:
        print("Wrong Input!! Try again")
    

    # fucntion definition 
    def expense_add():
        
        category = input("Enter your category")
        amount = validate_file(input("Enter the amount for the "))

        if amount is not None:
            data = read(EXPENSE_FILE)
            data.append({'category':category, 'amount':amount})
            write(EXPENSE_FILE, data)
            print("Expense added successfully! Hurrah!")


    def expense_view():
        data = read(EXPENSE_FILE)
        print("\n---EXPENSES---")
        for idx, expense in enumerate(data,1):
            print(f"{idx}.{expense['category']}: Rs{expense['amoumt']}")


    def expense_summary():
        total = calculate_total_expenses(EXPENSE_FILE)
        summary = calculate_category_summary(EXPENSE_FILE)
        print("\n---Total Expenses---")
        print("") 
    


    
