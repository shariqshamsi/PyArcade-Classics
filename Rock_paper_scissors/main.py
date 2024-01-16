import random

def play():
    user = input("Choose one from following:\n'R' for Rock, 'P' for Paper or 'S' for Scissors\n" )
    computer = random.choice(['R', 'P', 'S'])
    
    if user == computer :
        return "It's a tie"
    
    if is_win(user, computer):
        return 'You Won!'
    
    return 'You Lost!'
   
def is_win(player, opponent):
    if(player == 'R' and opponent == 'S') or (player == 'S' and opponent == 'P') \
        or ( player == 'P' and opponent == 'R') :
            return True


print(play())
