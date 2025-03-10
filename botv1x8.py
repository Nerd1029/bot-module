import time; import sys; import random

#VARIABLE BANK START
choices = ["Heads", "Tails"]
ChoicesG = ["", "", "", ""]
#VARIABLE BANK END

def inch(mm):
    x = mm / 25.4
    print(f"{mm}mm = ",x,"in", sep="")

def mm(inch):
    b = inch * 25.4
    print(f"{inch}in = ",b,"in", sep="")

def coinflip(times):
    for i in range(times):
        print(random.choice(choices), sep="\n")

def choice(ChoiceA, ChoiceB, ChoiceC, ChoiceD):
    ChoicesG = {ChoiceA}, {ChoiceB}, {ChoiceC}, {ChoiceD}
    return random.choice(ChoicesG)

def end(delay, msg):
    time.sleep(delay)
    sys.exit(f"{msg}")

def errormsg(msg):
    return f"{msg}"

def lock(p1, p2="", p3="", p4="", p5="", p6="", p7="", p8="", p9="", p10=""):
    x = input("ENTER PASSWORD HERE: ")
    if x == p1 or p2 or p3 or p4 or p5 or p6 or p7 or p8 or p9 or p10:
        print("ACCESS GRANTED")
    
    elif x != p1 or p2 or p3 or p4 or p5 or p6 or p7 or p8 or p9 or p10:
        sys.exit("ACCESS DENIED")

#Copyright © 2025 by Louis J. Bara Jr.