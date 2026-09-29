# Student Expense Tracker

A command-line Python program that helps students record their daily expenses, understand where their money goes, and get warned before they overspend.

## Overview

Many students run out of money before the month ends because they never track small daily expenses. This project lets a student record expenses, review them, analyse spending by category, and set a monthly budget that triggers warnings. It runs fully in the terminal and needs no extra libraries.

## Features

- Add, view, update and delete expenses (full CRUD)
- Expenses are saved to a text file, so data is kept after the program closes
- Analysis report: total spent, biggest expense, categories used, spending per category, kth largest expense
- Monthly budget with a warning at 80% and an alert when the limit is crossed
- Input validation: empty text, wrong number formats, zero or negative amounts and out-of-range row numbers are handled without crashing
- Menu-driven interface

## Technologies Used

- Python 3 (standard library only, no external packages)
- Git and GitHub for version control
- VS Code as the editor

## Python Concepts Used

Variables and expressions, conditionals (if / elif / else), while and for loops, functions with parameters and return values, modules and imports, lists, dictionaries, sets, string methods, file handling, exception handling (try / except), and basic array techniques (summation, finding the maximum, removing duplicates, kth largest element).

## Project Structure

```
expense_tracker/
├── main.py            menu and program flow
├── expenses.py        add, view, update, delete
├── analysis.py        totals, maximum, categories, kth largest
├── budget.py          budget status messages
├── validation.py      safe input functions
├── storage.py         save and load from a text file
├── README.md
└── statement.md
```

## How to Set Up and Run

1. Install Python 3.8 or newer from https://www.python.org and check it with:
```
   python --version
```
2. Download the project:
```
   git clone https://github.com/your-github-username/expense_tracker.git
   cd expense_tracker
```
3. There are no dependencies to install and no configuration is needed.
4. Run the program:
```
   python main.py
```
5. Follow the menu. Expenses are saved automatically in `expenses_data.txt`, which is created on first use.

## How to Test

Testing is done by running the program and trying these cases:

| Test | What to do | Expected result |
|------|------------|-----------------|
| Add expense | Option 1, enter Tea, 20, Food | "Expense added." |
| View | Option 2 | Numbered list shows Tea |
| Bad amount | Option 1, type `abc` as amount | Asks again, no crash |
| Negative amount | Option 1, type `-5` as amount | "Amount must be greater than zero." |
| Empty name | Option 1, press Enter for the name | "This cannot be empty." |
| Update | Option 3, number 1, new values | "Expense updated." |
| Wrong row number | Option 4, enter `99` | "That number does not exist." |
| Analysis | Add 3 expenses, option 5 | Total, biggest, categories and kth largest shown |
| Budget alert | Option 6 set 90, then add expenses past 90 | Warning at 80%, alert when over |
| Saving | Add an expense, exit, run again, option 2 | The expense is still there |

## Screenshots

[Add 3 or 4 screenshots of your terminal here: the menu, adding an expense, the analysis report, and a budget alert.]

## Author

Shourya Tiwari, CSE AIML, VIT Bhopal 26BAI10839
