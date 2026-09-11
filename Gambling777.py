#                             Gambling777 
# - A use of NumPy n Array and Learning a very low-level Game Structure -
#time.sleep used for to show a illusion of spinning roullette
#simultaneously columns must be spun
#few variables used to keep track of balance
#random used for no. of spin one column is going to do


# pyright: reportWildcardImportFromLibrary=false
from random import *
import time
from numpy import *


balance = 100
spin_cost = 10

def roller():

    column_1 = array(['$','&','7','N'])
    column_2 = array(['&','7','N','$'])
    column_3 = array(['7','N','$','&'])

    #spin
    l = randint(20,25)
    m = randint(32,37)
    n = randint(40,50)
    for i in range(n) :
        if i <= l :
            column_1 = roll(column_1, 1)
        if i<= m :
            column_2 = roll(column_2, 1)
        column_3 = roll(column_3, 1)

        display = array([
        [column_1[0],column_2[0],column_3[0]],
        [column_1[1],column_2[1],column_3[1]],
        [column_1[2],column_2[2],column_3[2]]
    ])    
        print(display, flush=True)
        if i <(n-1) :
            print("\033[3F", end="")
        time.sleep(0.2)
    c1d = column_1[1]
    c2d = column_2[1]
    c3d = column_3[1]

    return c1d,c2d,c3d

#intro
print("Hello There! You think you've got a Good Luck?")
time.sleep(2)
print("Only One way to find out.... ")
time.sleep(2)
print("Gambling! ")
time.sleep(2)
print("Welcome To The 777 Slot Machine!")
time.sleep(2)
print("Rules- \n Keep Gambling Until You Go Broke")
print("Or Maybe...")
time.sleep(5)
print("You Earn Something Rogue!")
print("good LUCK! \n")
time.sleep(3)

#Rules
r = input("Enter r/R for rules, otherwise anything")
if r == ("r" or 'R'):
     print("Your Balance is ", balance)
     time.sleep(2)
     print("One Spin Costs ", spin_cost)
     time.sleep(2)
     print("If two symbols matches, you earn 20 units, ")
     time.sleep(2)
     print("If all symbols same : N = 0, % = 60, $ = 70,... 7 = 100!")
     time.sleep(3)
     print("T&C Apply, .|.., those small dots are the T&C, go fuck yourself if you can't read it")
     time.sleep(8)
     print("Ready?")
     time.sleep(1)

#loop
while balance>0 :
    print("Current Balance - ", balance)
    time.sleep(2)

    if input("Spin? Press Enter, Or to Stop input anything and Enter") == "": 
        balance = balance - spin_cost
        cd = tuple(roller())
        if cd[0]==cd[1]==cd[2]=="7" :
            balance= balance + 110
            print("JACKPOT!")
        elif cd[0]==cd[1]==cd[2]=="$" :
                        balance= balance + 80
        elif cd[0]==cd[1]==cd[2]=="%" :
                        balance= balance + 70
        elif cd[0]==cd[1]==cd[2]=="N" :
                        print("Luckily Unlucky, Noob")
                        time.sleep(2)
        elif cd[0]==cd[1] or cd[0]==cd[2] or cd[2]==cd[1] :
                    balance = balance + 30
    else :
         time.sleep(1)
         print("\n That's it? I thought you were going to earn more profit....... For me XD")
         print("Your balance : ", balance)
         break
if balance <= 0 :
       time.sleep(1)
       print("Broke.. Sed Life")
       time.sleep(2)
       print("Skill Issue")
time.sleep(1)

#highscorer
try:
    with open("highscore.txt", "r") as file:
        highscore = int(file.read())
except FileNotFoundError:
    highscore = 0

score = balance

if score > highscore:
    highscore = score

    with open("highscore.txt", "w") as file:
        file.write(str(highscore))

    print("NEW HIGH SCORE!")
else:
    print("High score:", highscore)

#no problemo, working as intended, Bravo!