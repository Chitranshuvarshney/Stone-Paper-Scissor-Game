import random

# This is the stone, Paper & Scissor Game!

def gameWin(comp, you):
    if comp == you:
        return None
    elif comp == 'stone':
        if you=='paper':
            return True
        elif you=='scissor':
            return False
    elif comp == 'paper':
        if you=='stone':
            return False
        elif you=='scissor':
            return True
    elif comp == 'scissor':
        if you=='stone':
            return True
        elif you=='paper':
            return False

print("Comp Turn: stone, paper, scissor? ")
randNo = random.randint(1, 3)
if randNo == 1:
    comp = 'stone'
elif randNo == 2:
    comp = 'paper'
elif randNo == 3:
    comp = 'scissor'

you = input("Your Turn: stone, paper, scissor? ")

a = gameWin(comp, you)

print("Computer Choose:", comp)
print("You Choose:", you)

if you!= "stone" and you!= "paper" and you!= "scissor":
    print("You Choose Wrong Input!")
elif a==None:
    print("The game is Tie!")
elif a:
    print("You Win!")
else:
    print("You Lose!")