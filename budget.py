def check_budget(total, limit):
    if limit <= 0:
        return "No budget set yet."
    percent = round(total / limit * 100, 1)
    if total > limit:
        over = round(total - limit, 2)
        return "ALERT: You are over budget by " + str(over)
    elif percent >= 80:
        return "Warning: You have used " + str(percent) + "% of your budget."
    else:
        return "Good: You have used " + str(percent) + "% of your budget."