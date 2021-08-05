import random as ran
import time
print("Welcome To Our Snake,Water,Gun Game")
time.sleep(1)
Draws=0
Wins=0
Loses=0
loop=10
liste=["s","w","g"]
for a in range(1,loop):
    rand=ran.choice(liste)
    user_inp=input(str(a)+ ":""Enter 's' For Snake\n 'w' For Water\n 'g' For Gun\n ")
    if(str(rand)=="s"):
        if(user_inp=="s"):
            print("Draw")
            Draws=Draws+1
        elif(user_inp=="w"):
            print("Lose")
            Loses=Loses+1
        elif(user_inp=="g"):
            print("Win")
            Wins=Wins+1
    if(str(rand)=="w"):
        if(user_inp=="s"):
            print("Win")
            Wins=Wins+1
        if(user_inp=='w'):
            print("Draw")
            Draws=Draws+1
        if(user_inp=='g'):
            print("Lose")
            Loses=Loses+1
    if(str(rand)=="g"):
        if(user_inp=='s'):
            print("Lose")
            Loses=Loses+1
        if(user_inp=='w'):
            print("Win")
            Wins=Wins+1
        if(user_inp=='g'):
            print("Draw")
            Draws=Draws+1
print("Fetching Results")
time.sleep(3)
if(Wins>Loses):
    print("You Won Overall")
elif(Loses>Wins):
    print("You Lost Overall")
elif(Loses==Wins):
    print("Draw Overall")
