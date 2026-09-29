import expenses
import analysis
import budget
import storage
import validation

monthly_limit = 0
expenses.expense_list.extend(storage.load_expenses())


def show_menu():
    print("\n1. Add expense")
    print("2. View expenses")
    print("3. Update expense")
    print("4. Delete expense")
    print("5. Analysis report")
    print("6. Set monthly budget")
    print("7. Check budget")
    print("8. Exit")


while True:
    show_menu()
    choice = input("Enter your choice: ").strip()

    if choice == "1":
        name = validation.get_text("Expense name: ")
        amount = validation.get_amount("Amount: ")
        category = validation.get_text("Category: ")
        expenses.add_expense(name, amount, category)
        storage.save_expenses(expenses.expense_list)
        print("Expense added.")
        total = analysis.total_spent(expenses.expense_list)
        print(budget.check_budget(total, monthly_limit))
    elif choice == "2":
        expenses.view_expenses()
    elif choice == "3":
        expenses.view_expenses()
        if len(expenses.expense_list) > 0:
            number = validation.get_whole_number("Enter the number to update: ")
            name = validation.get_text("New name: ")
            amount = validation.get_amount("New amount: ")
            category = validation.get_text("New category: ")
            if expenses.update_expense(number, name, amount, category):
                storage.save_expenses(expenses.expense_list)
                print("Expense updated.")
            else:
                print("That number does not exist.")
    elif choice == "4":
        expenses.view_expenses()
        if len(expenses.expense_list) > 0:
            number = validation.get_whole_number("Enter the number to delete: ")
            if expenses.delete_expense(number):
                storage.save_expenses(expenses.expense_list)
                print("Expense deleted.")
            else:
                print("That number does not exist.")
    elif choice == "5":
        data = expenses.expense_list
        if len(data) == 0:
            print("Add some expenses first.")
        else:
            print("Total spent:", analysis.total_spent(data))
            biggest = analysis.highest_expense(data)
            print("Biggest expense:", biggest["name"], biggest["amount"])
            print("Categories used:", analysis.unique_categories(data))
            print("Spending per category:", analysis.category_totals(data))
            k = validation.get_whole_number("Show the kth largest expense, k = ")
            result = analysis.kth_largest(data, k)
            if result is None:
                print("k is out of range.")
            else:
                print("Kth largest expense:", result)
    elif choice == "6":
        monthly_limit = validation.get_amount("Enter your monthly budget: ")
        print("Budget set to", monthly_limit)
    elif choice == "7":
        total = analysis.total_spent(expenses.expense_list)
        print("Total spent:", total)
        print(budget.check_budget(total, monthly_limit))
    elif choice == "8":
        print("Goodbye!")
        break
    else:
        print("Invalid choice, try again.")