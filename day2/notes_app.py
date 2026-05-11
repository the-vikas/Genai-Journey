#take input from user
user_input = input("Enter what's in your mind to save in file: ")

if user_input.strip() == "":
    print("Notes can't be eampty.")

else:
    #now append user input to file
    with open("./notes.txt", "a") as text_file:
        text_file.write("\n" + user_input)

    #Read all the notes and display
    with open("./notes.txt", "r") as read_file:
        print("\nSaved Notes:")
        print(read_file.read())
