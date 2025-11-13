import getpass
import time

def rock_paper_scissors_game(Player1, Player2):
    if Player1 == 'rock' and Player2 == 'scissors':
        print('Player1 wins!')
    elif Player1 == 'paper' and Player2 == 'rock':
        print('Player1 wins!')
    elif Player1 == 'scissors' and Player2 == 'paper':
        print('Player1 wins!')
    elif Player1 == Player2:
        print('DRAW!')
    else:
        print('Player2 wins!')

def main():
    print("\nWelcome to Rock, Paper, Scissors!")
    print("Type 'rock', 'paper', or 'scissors'. Let's begin!\n")
    time.sleep(1)

    Player1 = getpass.getpass('Player1, enter your choice (hidden): ')
    Player2 = getpass.getpass('Player2, enter your choice (hidden): ')

    print("\nRock...")
    time.sleep(0.6)
    print("Paper...")
    time.sleep(0.6)
    print("Scissors...")
    time.sleep(0.6)
    print("SHOOT!\n")
    time.sleep(0.4)

    rock_paper_scissors_game(Player1.lower(), Player2.lower())

main()
