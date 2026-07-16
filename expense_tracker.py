print("========== Expense Tracker ==========")

total = 0

while True:
    expense = input("Enter expense (or type 'done' to finish): ")

    if expense.lower() == "done":
        break

    total = total + float(expense)

print("\nTotal Amount Spent =", total)

print("Thank you for using Expense Tracker!")
