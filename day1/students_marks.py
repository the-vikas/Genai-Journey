name = input("Enter your name: ")
subject1 = float(input("Enter subject 1 makrs: "))
subject2 = float(input("Enter subject 2 marks: "))
subject3 = float(input("Enter subject 3 marks: "))

average = (subject1 + subject2 + subject3)/3
print(f"Student Name: {name}")
print(f"Average Marks: {average}")

if average >= 90:
    print("A Grade")

elif average > 75:
   print("B Grade")

elif average > 60:
    print("C Grade")

elif average <= 60:
    print("Fail")