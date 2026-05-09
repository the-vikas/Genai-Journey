num1 = float(input("Enter 1st Number: "))
num2 = float(input("Enter 2nd Number: "))

operation = input("Enter Operation(+,-,/,*): ")

if operation == "+":
    add = num1+num2
    print(f"Addition of both number is : {add}")

elif operation == "-":
    sub = num1-num2
    print(f"Sbstraction of both number is : {sub}")

elif operation == "*":
    multi = num1*num2
    print(f"Multiplication of both number is {multi}")

elif operation == "/":
    if num2 != 0:
        div = num1/num2
        print(f"Division of both number is : {div}")
    else:
        print("Error: Can't devide by 0")