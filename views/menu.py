# importing the library from the the other python files of the directory. 
# libraries that are not installed are imported and installed using the requirement text file. 

from utils.file_operation_file import read, write
from utils.validation_file import validate_file
from utils.summmary import calculate_total_expenses,calculate_category_summary
from colorama import Fore,Style,init
import time
THEME = Fore.WHITE

# initializing colorama
init(autoreset= True)

# json files are referenced here to use it. 

EXPENSE_FILE="data\\expenses.json"
CATEGORIES_FILE="data\\categories.json"

 

def print_header(title):
    print(Fore.CYAN + Style.BRIGHT + f"\n{'-' * 40}")
    print(Fore.CYAN + Style.Bright + f"{title.center(40)}")
    print(Fore.CYAN + Style.BRIGHT + f"{'-'*40}")

def print_divider():
    print(Fore.MAGENTA + '-'*40)

# the diplay function is created with the necessary menues of the program and choice

def display_menu():
    print("====================================")
    print("     Personal Expense Tracker")
    print("====================================")
    print(Fore.GREEN + "1. Add Expenses")
    print(Fore.YELLOW +"2. View Expenses")
    print(Fore.BLUE +"3.View Summary")
    print(Fore.RED+"4. Move Out")
    print_divider()
    
    choice = int(input(Fore.CYAN +"Enter your choice "))

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



# fucntion definition of the above choices 
def expense_add():
        
        category = input("Enter your category in respect to the below category")
        print("Food", "Travel","Bills","Investment","Miscellaneous")
        amount = validate_file(input("Enter the amount for the "))

        if amount is not None:
            show_loading("Saving Expense")
            data = read(EXPENSE_FILE)
            data.append({'category':category, 'amount':amount})
            write(EXPENSE_FILE, data)
            print("Expense added successfully! Hurrah!")


def expense_view():
        data = read(EXPENSE_FILE)
        print("\n---EXPENSES---")
        for idx, expense in enumerate(data,1):
            print(f"{idx}.{expense['category']}: Rs {expense['amount']}")


def expense_summary():
        total = calculate_total_expenses(EXPENSE_FILE)
        summary = calculate_category_summary(EXPENSE_FILE)
        print("\n---Summary---")
        print(f'Total Expenses: Rs {total}' )
        for category,amount in summary.items():
            print(f"{category}: Rs {amount}")

# colorlama function for making the user show that data is being loaded. 

def show_loading(message= "Processing"):
    print(Fore.YELLOW + message,end="")
    for _ in range(3):
        time.sleep(0.5)
        print(Fore.YELLOW + ".", end = "")
    print("\n")

#  setting up the theme 

def set_theme(color):
    global THEME
    themes = {'blue':Fore.BLUE, 'green':Fore.GREEN, 'red':Fore.RED}
    THEME = themes.get(color.lower(),Fore.WHITE)

def print_colored(text):
    print(THEME + text)