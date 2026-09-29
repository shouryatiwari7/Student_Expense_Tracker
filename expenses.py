expense_list = []


def add_expense(name, amount, category):
    expense = {"name": name, "amount": amount, "category": category}
    expense_list.append(expense)


def view_expenses():
    if len(expense_list) == 0:
        print("No expenses added yet.")
        return
    number = 1
    for expense in expense_list:
        print(number, expense["name"], expense["amount"], expense["category"])
        number = number + 1


def update_expense(number, name, amount, category):
    if number < 1 or number > len(expense_list):
        return False
    expense_list[number - 1] = {"name": name, "amount": amount, "category": category}
    return True


def delete_expense(number):
    if number < 1 or number > len(expense_list):
        return False
    expense_list.pop(number - 1)
    return True