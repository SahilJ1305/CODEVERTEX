import random

def DisplayScore(a, b):
    print("Your Score:", a)
    print("Computer Score:", b)

Userpoints = 0
Computerpoints = 0
Options = ["R", "P", "S"]
while True:
    print("Lets play a game of rock paper and scissors")
    print("Enter R for Rock")
    print("Enter P for Paper")
    print("Enter S for Scissor")
    print("Enter D for Display Score")
    print("Enter E for Exit")
    user_choice = input("Enter your choice:")
    computer_choice = random.choice(["R", "P", "S"])

    if user_choice == "R":
        if computer_choice == "R":
            print("It's a tie")
        elif computer_choice == "P":
            print("Computer Wins")
            Computerpoints += 1
            print("Computer Choice:", computer_choice)
        elif computer_choice == "S":
            print("You Win")
            Userpoints += 1
            print("Computer Choice:", computer_choice)

    elif user_choice == "P":
        if computer_choice == "P":
            print("It's a tie")
        elif computer_choice == "S":
            print("Computer Wins")
            Computerpoints += 1
            print("Computer Choice:", computer_choice)
        elif computer_choice == "R":
            print("You Win")
            Userpoints += 1
            print("Computer Choice:", computer_choice)

    elif user_choice == "S":
        if computer_choice == "S":
            print("It's a tie")
        elif computer_choice == "R":
            print("Computer Wins")
            Computerpoints += 1
            print("Computer Choice:", computer_choice)
        elif computer_choice == "P":
            print("You Win")
            Userpoints += 1
            print("Computer Choice:", computer_choice)

    elif user_choice == "D":
        DisplayScore(Userpoints, Computerpoints)

    elif user_choice == "E":
        print("Thanks for playing")
        exit()

    else:
        print("Invalid Input")
