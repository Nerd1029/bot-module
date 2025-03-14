import time; import sys; import random; import colorama; from colorama import Fore, Back, Style

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

def lock(p1, rc):
    x = input(f"{Fore.WHITE}ENTER PASSWORD HERE: ")
    if x == p1:
        print(f"{Fore.GREEN}ACCESS GRANTED")
    
    elif x != p1:
        r = input(f"{Fore.RED}ACCESS DENIED")
        if r == rc:
            print(f"{Fore.GREEN}ACCESS RECOVERED")
        elif r != rc:
            sys.exit(f"{Fore.WHITE}ACCESS DENIED")

def copyrightclaim(year, name):
    print(f"{Fore.WHITE}Copyright © {year} by {name}. ALL RIGHTS RESERVED.")

    def tmclaim(Brandname, registeredstatus, isSM):
        if isSM == "Yes":
            print(f"{Fore.WHITE}{Brandname}℠")
        
        elif isSM == "No":
            pass
        
        if registeredstatus == "No":
            print(f"{Fore.WHITE}{Brandname}™")
        elif registeredstatus == "Yes":
            print(f"{Fore.WHITE}{Brandname}®")

#Copyright © 2025 by Louis J. Bara Jr. ALL RIGHTS RESERVED.