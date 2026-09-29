def total_spent(expense_list):
    total = 0
    for expense in expense_list:
        total = total + expense["amount"]
    return total


def highest_expense(expense_list):
    if len(expense_list) == 0:
        return None
    highest = expense_list[0]
    for expense in expense_list:
        if expense["amount"] > highest["amount"]:
            highest = expense
    return highest


def unique_categories(expense_list):
    categories = set()
    for expense in expense_list:
        categories.add(expense["category"])
    return categories


def category_totals(expense_list):
    totals = {}
    for expense in expense_list:
        category = expense["category"]
        if category in totals:
            totals[category] = totals[category] + expense["amount"]
        else:
            totals[category] = expense["amount"]
    return totals


def kth_largest(expense_list, k):
    if k < 1 or k > len(expense_list):
        return None
    amounts = []
    for expense in expense_list:
        amounts.append(expense["amount"])
    amounts.sort(reverse=True)
    return amounts[k - 1]