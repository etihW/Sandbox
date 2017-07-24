import time
from random import randint

def comp_pick():
    val = randint(1,3)
    if val == 1:
        hand = "rock"
    elif val == 2:
        hand = "scissors"
    elif val == 3:
        hand = "paper"
    return hand


def compare_hands(comp, you):
    if comp == you:
        winner = "tie"
    elif comp == ('rock' and you == 'scissors') or (comp == 'scissors' and you == 'paper')\
        or (comp == 'paper' and you == 'rock'):
        winner = 'computer'
    else:
        winner = 'you'
    return winner


def main():
    playing = True
    print("Let's play Scissors, Paper, and rock!\n")
    while playing:
        print("-\n")
        you = input("Type in rock, paper, or scissors. Type quit to end game\n")
        you = you.lower()
        if you == "quit":
            playing = False
        elif you == "paper" or you == "rock" or you == "scissors":
            comp = comp_pick()
            winner = compare_hands(comp, you)
            print("The computer played %s, you played %s" % (comp, you))
        else:
            print("Invalid entry, please try once more\n")
            continue
        if winner == "tie":
            print("You tied\n")
        elif winner == "computer":
            print("The computer won!\n")
        elif winner == "you":
            print("A winner is you!\n")
        print()
    print()

main()
