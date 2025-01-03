# Personal-Expense-Tracker

## 📋 Project Description

The **Personal Expense Tracker** is a console-based Python application designed to help users manage and track their daily expenses. It allows users to:
- Add expenses categorized by type (e.g., Food, Travel, etc.).
- View a detailed list of recorded expenses.
- Get a summarized view of expenses by category.

This project demonstrates Python concepts like file handling, modular programming, and unit testing.

---

## 🎯 Features
- **Add Expense**: Save categorized expenses with a specified amount.
- **View Expenses**: Display all recorded expenses in an organized format.
- **Expense Summary**: Summarize total expenses by category.
- **Data Persistence**: All data is saved in JSON files for future use.

---

## 📂 Project Structure

personal_expense_tracker/
│
├── main.py                # Entry point for the application
│
├── data/                  # Stores all persistent data
│   ├── expenses.json      # JSON file to store expenses
│
├── utils/                       # Helper functions and modules
│   ├── file_operation_file.py   # Functions for reading and writing data
│   ├── summary.py               # Functions to calculate summaries
│
├── views/                 # Handles console interface
│   ├── menu.py            # Main menu display logic
│
├── tests/                 # Testing files
│   ├── test_file_ops.py   # Unit tests for file operations
│
├── docs/                  # Documentation files
│   ├── README.md          # Main project description
│
├── requirements.txt       # Dependencies for the project

## 🔨 To Run the Application
    python main.py

## 📩 Install Requirement Text File
    pip install -r requirements.txt

##  🔨 To Run the Test Files
    python -m unittest tests//test_file.py

