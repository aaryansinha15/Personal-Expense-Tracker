from utils.file_operation_file import read

def calculate_total_expenses(directory):
    data = read(directory)
    return sum(expense['amount'] for expense in data)

def calculate_category_summary(directory):
    data = read(directory)(directory)
    summary = {}
    for expense in data:
        category = expense['category']
        summary[category]= summary.get(category,0)+expense['amount']
    return summary