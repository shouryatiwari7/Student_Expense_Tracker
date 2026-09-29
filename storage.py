def save_expenses(expense_list, filename="expenses_data.txt"):
    file = open(filename, "w")
    for expense in expense_list:
        line = expense["name"] + "," + str(expense["amount"]) + "," + expense["category"]
        file.write(line + "\n")
    file.close()


def load_expenses(filename="expenses_data.txt"):
    loaded = []
    try:
        file = open(filename, "r")
    except FileNotFoundError:
        return loaded
    for line in file:
        line = line.strip()
        if line == "":
            continue
        parts = line.split(",")
        if len(parts) != 3:
            continue
        loaded.append({"name": parts[0], "amount": float(parts[1]), "category": parts[2]})
    file.close()
    return loaded