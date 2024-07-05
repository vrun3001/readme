import random
choice = ["Snake", "Water", "Gun"]
computer = input("Please enter a number between 'Snake, 'Water, 'Gun'")
player = input("Please enter a number between 'Snake, 'Water, 'Gun'")
if computer == player:
    print("Game draw, No body won there")
comp_win = 0

user_win = 0
if computer == 'Snake':
    if player == 'Water':
        comp_win += 1
    elif player == 'Gun':
        user_win += 1

elif computer == 'Water':
    if player == 'Gun':
        comp_win += 1
    elif player == 'Snake':
        user_win += 1

elif computer == 'Gun':
    if player == 'Snake':
        comp_win += 1
    elif player == 'Water':
        user_win += 1
if user_win > comp_win:
    print(f"You Won Game")
elif comp_win > user_win:
    print(f"Computer Won Game")
else:
    print("Draw!!\n")