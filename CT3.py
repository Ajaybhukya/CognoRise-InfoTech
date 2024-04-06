import random
def determine_winner(user_choice,computer_choice):
    if user_choice == computer_choice:
        return "Tied"
    elif (user_choice == "rock" and computer_choice == "scissor" or
        user_choice == "paper" and computer_choice == "rock" or
        user_choice == "scissor" and computer_choice == "paper"):
        return "You won the game"
    else:
        return "Computer won the game"
def computer_choice():
    return random.choice(['rock', 'paper', 'scissor'])
choice=input("Read your choice[Rock,paper or scissor]:").lower()
while choice not in ['rock','paper','scissor']:
    print("Invalid choice! Re-enter your choice")
    choice=input("Read your choice[Rock,paper or scissor]:")
print("You choice ",choice)
computer_ch=computer_choice()
print("Computer choice is",computer_ch)
print(determine_winner(choice,computer_ch))