import random

def play():
    user = input("Qu'avez vous choisi ? 'r' pour rock, 'p' pour paper, 's' pour scissors\n")
    computer = random.choice(['r','p','s'])
    
    if user == computer:
        return 'It\'s a tie'
    
    
    if is_win(user, computer):
        return 'You won !'
    
    return 'You lost !'
    
def is_win(player, opponent):
    # r > s, s > p, p > r 
    # retourne True si un joueur gagne
    
    if(player == 'r' and opponent =='s') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True

print(play())