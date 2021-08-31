#Rock Paper Scissor
import random
import sys

choice = ["Rock","Paper","Scissors"]

computer = random.choice(choice)
temp = "Yes"

while temp == "Yes" or temp == "Y" or temp == "yes" or temp =="y":
    print("Rock, Paper, Scissors?")
    user_input = input("What do you choose:\n")
    if user_input == "Rock":
        if computer == "Paper":
            print("You win, Paper covers Rock")
            temp = str(input("You wana play again?\nYes or No\n"))
        elif computer == "Rock":
            print("Tie")
            temp = str(input("You wana play again?\nYes or No\n"))
        elif computer == "Scissors":
            print("You lost, Rock smashes Scissors")
            temp = str(input("You wana play again?\nYes or No\n"))
        else:
            print("Invalid Input!")
            temp = str(input("You wana try again?\nYes or No\n"))


    elif user_input == "Paper":
        if computer == "Scissors":
            print("You win, Scissors cut Paper")
            temp = str(input("You wana play again?\nYes or No\n"))
        elif computer == "Paper":
            print("Tie")
            temp = str(input("You wana play again?\nYes or No\n"))
        elif computer == "Rock":
            print("You lost, Paper covers Rock")
            temp = str(input("You wana play again?\nYes\nNo\n"))
        else:
            print("Invalid Input!")
            temp = str(input("You wana try again?\nYes or No\n"))


    elif user_input == "Scissors":
        if computer == "Rock":
            print("You win, Rock smashes Scissors")
            temp = str(input("You wana play again?\nYes or No\n"))
        elif computer == "Scissors":
            print("Tie")
            temp = str(input("You wana play again?\nYes or No\n"))
        elif computer == "Paper":
            print("You lost, Scissors cut Paper")
            temp = str(input("You wana play again?\nYes or No\n"))
        else:
            print("Invalid Input!")
            temp = str(input("You wana try again?\nYes or No\n"))
    else:
        print("Invalid Input")

    if temp == "No" or temp == "N" or temp == "no" or temp =="n":
        sys.exit()
    else:
        print("Invalid Input!")
        temp = str(input("Only give: Yes or No\n"))