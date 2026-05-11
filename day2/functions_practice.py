def add_number(a, b):
    return a+b

def sub_number(a, b):
    return a-b

def average_number(a, b):
    return (a+b) / 2

num1 = float(input("Enter 1st number: "))
num2 = float(input("Enter 2nd number: "))

addition = add_number(num1, num2)
subtraction = sub_number(num1, num2)
average = average_number(num1, num2)

print("\nResults")
print(f"Addition of both numbers is: {addition}")
print(f"Subtraction of both numbers is: {subtraction}")
print(f"Average of both numbers is: {average:.2f}")
print("Thank you for calculating here!")