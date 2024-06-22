import random
import colorama
from colorama import Fore, Style
colorama.init(autoreset=True) # Initializing colorama to automatically reset color settings

# Function to simulate rolling a dice
def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)

    return roll


# Asking for number of players, ensuring it's between 2 and 4
while True:

    players = input("Enter the number of players (2 - 4): ")
    print()

    if players.isdigit():
        players = int(players)

        if 2 <= players <= 4 :
            break
        else:
            print("Players must be between 2 - 4.")
    else:
        print("Invaild, Please try again.")


# Setting the maximum score to reach to win the game
max_score = 50
players_score = [0 for _ in range(players)] # Initializing scores for each player to zero

# Loop to continue the game until someone reaches the maximum score
while  max(players_score) < max_score:

   # Looping through each player's turn
   for player_idx in range(players):

       print(Fore.MAGENTA + Style.BRIGHT + f"Player number {player_idx + 1} turn has just started!")
       print(f"Your total score is : {players_score[player_idx]} \n")
       current_score = 0

       # Inner loop for each player to roll the dice
       while True:
            should_roll = input(Fore.BLACK + Style.BRIGHT + "Would you like to roll (y/n)? ")
            if should_roll.lower() != "y":
                break

            value = roll()   # Roll the dice and get a random value
            if value == 1:
                print(Fore.RED + "You rolled a 1!, Turn done!")
                current_score = 0
                break
            else:
                current_score += value  # Add the rolled value to the current score
                print("You rolled a: ",value)

            print(f"Your score is: {current_score}")

       players_score[player_idx] += current_score    # Add the current score to the player's total score
       print(f"Your total score is: {players_score[player_idx]} ")
       print()

max_score = max(players_score) # Determine the maximum score among all players
winnig_idx = players_score.index(max_score)   # Find the index of the player with the maximum score (the winner)
print(Fore.BLUE + f"Player number {winnig_idx + 1} is the winner\U0001F3C6 with the score of: {max_score}")