expenses = []

while True:
    expense = float(input("Enter Your Expense: "))
    expenses.append(expense)

    choice = input("Add More Expense? (yes/no): ").lower()
    if choice == "no":
        break

total = sum(expenses)
highest = max(expenses)
average = total / len(expenses)

print(f"\nTotal Expenses: {total}")
print(f"Highest Expense: {highest}")
print(f"Average Expense: {average:.2f}") #.2f means: show only 2 decimal places.