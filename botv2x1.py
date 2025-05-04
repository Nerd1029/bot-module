import time; import sys; import random; import colorama; from colorama import Fore, Back, Style; import tqdm; import os; import subprocess

#VARIABLE BANK START
choices = ["Heads", "Tails"]
ChoicesG = ["", "", "", ""]
e403 = "ERROR 403 FORBIDDEN"
e404 = "ERROR 404 REQUESTED ITEM NOT FOUND"
#VARIABLE BANK END

def accessD(ending):
    os.system(f'say "ACCESS DENIED{ending}"')

def accessG(end):
    os.system(f'say "ACCESS GRANTED{end}"')

print("\n")

print("Installing main packages...")
for i in tqdm.tqdm(range(150000000), desc="Progress", colour="yellow"):
    continue

print("\n")

print("Preparing main code...")
for i in tqdm.tqdm(range(100000000), desc="Progress", colour="green"):
    continue

print("\n")

print("Installing classes...")
for i in tqdm.tqdm(range(230000000), desc="Progress", colour="red"):
    continue

print("\nThe following program uses the bot module which IS copyrighted as seen below:\nCopyright © 2025 by Louis J. Bara Jr. ALL RIGHTS RESERVED.\n")

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

def end(delay, code):
    time.sleep(delay)
    sys.exit(f"{code}")

def errormsg(codeB, end):
    if end == "T":
        sys.exit({codeB})
    elif end == "F":
        return f"{codeB}"

def lock(password, rc):
    x = input(f"{Fore.WHITE}ENTER PASSWORD HERE: ")
    if x == password:
        print(f"{Fore.GREEN}ACCESS GRANTED"); accessG("!")

    elif x != password:
        r = input(f"{Fore.RED}ACCESS DENIED")
        accessD()
        
        if r == rc:
            print(f"{Fore.GREEN}ACCESS RECOVERED")
        elif r != rc:
            sys.exit(f"{Fore.RED}ACCESS DENIED")

def copyrightclaim(year, name):
    print(f"{Fore.WHITE}Copyright © {year} by {name}. ALL RIGHTS RESERVED.")

def tmclaim(Brandname, registeredstatus, isSM):
    if isSM == "Yes" or "yes":
            print(f"{Fore.WHITE}{Brandname}℠")
        
    elif isSM == "No" or "no":
        pass
        
    if registeredstatus == "No":
        print(f"{Fore.WHITE}{Brandname}™")
    elif registeredstatus == "Yes":
        print(f"{Fore.WHITE}{Brandname}®")

def test(runcount):
    x = input("ENTER ACCESS CODE HERE: ")
    
    if x == "2204":
        for i in range(runcount):
            inch(22)
            mm(22)
            coinflip(10)
            choice("a", "b", "c", "d")
            lock("aaa", "bbb")
            copyrightclaim("XXXX", "SAMPLE")
            tmclaim("Nerd Corp", "Yes", "No")
            
            y = input("")
            
            if y == "T, T":
                tmclaim("SAMPLE", "Yes", "Yes")
            
            elif y == "F, T":
                tmclaim("SAMPLE", "No", "Yes")
            
            elif y == "T, F":
                tmclaim("SAMPLE", "Yes", "No")
            
            elif y == "F, F":
                tmclaim("SAMPLE", "No", "No")
            
            z = input("")

            if z == "e403":
                end(2, e403)
            
            elif z == "e404":
                end(2, e404)
            
            c = input("")

            if c == "3642":
                d = input("")
                if d == "e403":
                    errormsg(e403, "T")
                
                elif d == "e404":
                    errormsg(e404, "F")

class ts:
    
    fullreset = colorama.Style.RESET_ALL

    class text:
        green = colorama.Fore.GREEN
        red = colorama.Fore.RED
        blue = colorama.Fore.BLUE
        cyan = colorama.Fore.CYAN
        magenta = colorama.Fore.MAGENTA
        yellow = colorama.Fore.YELLOW
        white = colorama.Fore.WHITE
        Lred = colorama.Fore.LIGHTRED_EX
        Lwhite = colorama.Fore.LIGHTWHITE_EX
        Lblack = colorama.Fore.LIGHTBLACK_EX
        Lblack = colorama.Fore.LIGHTBLACK_EX
        Lcyan = colorama.Fore.LIGHTCYAN_EX
        Lgreen = colorama.Fore.LIGHTGREEN_EX
        Lmagenta = colorama.Fore.LIGHTMAGENTA_EX
        Lyellow = colorama.Fore.LIGHTYELLOW_EX
        Creset = colorama.Fore.RESET



    class back:
        black = colorama.Back.BLACK
        green = colorama.Back.GREEN
        blue = colorama.Back.BLUE
        cyan = colorama.Back.CYAN
        magenta = colorama.Back.MAGENTA
        yellow = colorama.Back.YELLOW
        red = colorama.Back.RED
        Lblack = colorama.Back.LIGHTBLACK_EX
        Lblue = colorama.Back.LIGHTBLUE_EX
        Lgreen = colorama.Back.LIGHTGREEN_EX
        Lcyan = colorama.Back.LIGHTCYAN_EX
        Lmagenta = colorama.Back.LIGHTMAGENTA_EX
        Lyellow = colorama.Back.LIGHTYELLOW_EX
        Lwhite = colorama.Back.LIGHTWHITE_EX
        Lred = colorama.Back.LIGHTRED_EX
        Breset = colorama.Back.RESET

    class style:
        bright = colorama.Style.BRIGHT
        dim = colorama.Style.DIM
        normal = colorama.Style.NORMAL
    
class updater:
    a = input("Please remember to replace all dots i the versio name with 'x'. Enter the name of the version here: ")

    def update_package(a):
        subprocess.run([sys.executable, '-m', 'pip', 'install', '--upgrade', a])

    upd = update_package(a)

#Copyright © 2025 by Louis J. Bara Jr. ALL RIGHTS RESERVED.