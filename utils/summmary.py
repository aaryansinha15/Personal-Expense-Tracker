# importing the file_operation module to use the read fucntion of it.
from utils.file_operation_file import read

# function to calculate total expense by reading the expense file. 

def calculate_total_expenses(directory):
    data = read(directory)
    return sum(expense['amount'] for expense in data)

# function to calculate category by reading the category file
def calculate_category_summary(directory):
    data = read(directory)
    summary = {}
    for expense in data:
        category = expense['category']
        summary[category]= summary.get(category,0)+expense['amount']
    return summary