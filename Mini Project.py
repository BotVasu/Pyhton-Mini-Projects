#Rock Paper Scissor

from random import randint

choice = ["Rock","Paper","Scissors"]

computer = choice[randint(0,2)]

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
            temp = str(input("You wana play again?\n1.Yes\n2.No\n"))
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