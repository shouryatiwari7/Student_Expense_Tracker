def get_text(prompt):
    while True:
        text = input(prompt).strip()
        if text == "":
            print("This cannot be empty.")
        elif "," in text:
            print("Please do not use commas.")
        else:
            return text


def get_amount(prompt):
    while True:
        try:
            value = float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")
            continue
        if value <= 0:
            print("Amount must be greater than zero.")
        elif value > 10000000:
            print("That amount is too large.")
        else:
            return value


def get_whole_number(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a whole number.")