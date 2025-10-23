import pwinput




def rock_paper_scissors_game(Player1, Player2):
    
    if (Player1== 'rock' and Player2== 'scissors'):
        print('Player1 wins!')
    elif (Player1== 'paper' and Player2== 'rock'):
        print('Player1 wins!')
    elif (Player1== 'scissors'and Player2== 'paper'):
        print('Player1 wins!')

    elif (Player1== Player2):
        print('DRAW!')

    else:
        print('Player2 wins!')

# def validate(val):

def main():
    Player1=input('Player1 enter ')
    # validate(Player1)                               
    Player2=input('Player2 enter ')
    
    

    rock_paper_scissors_game(Player1, Player2)
main()