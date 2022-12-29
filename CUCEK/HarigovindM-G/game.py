#game of rock paper siccor

import random
import time

l=["R","P","S"]

# fucntion used for converting R,S,P
def converter(play):
    if play=='R':
        return 'ROCK'
    elif play=='S':
        return 'SCISSORS'
    elif play=='P':
        return 'PAPER'


while True:
    user_play=input("Enter your hand ROCK(R),PAPER(P),SCISSORS(S)")
    cpu_play=l[random.randint(0,2)]
    cpu_choice=converter(cpu_play)
    time.sleep(0.5)
    print("Computer played {}".format(cpu_choice))
    if user_play=="R":
        if cpu_play=="R":
            print("---DRAW---")
        elif cpu_play=='P':
            print("Computer wins!")
        elif cpu_play=="S":
            print("You win!")
    elif user_play=='P':
        if cpu_play=='P':
            print("---DRAW---")
        elif cpu_play=="R":
            print("You win!")
        elif cpu_play=='S':
            print("Computer wins!")
    elif user_play=='S':
        if cpu_play=='S':
            print("---DRAW---")
        elif cpu_play=="P":
            print("You win!")
        elif cpu_play=='R':
            print("Computer wins!")
    else:
        print("ENTER VALID INPUT")


