import random
import datetime
import time
import os

colourlist = ["RED", "ORANGE", "YELLOW", "GREEN", "BLUE", "WHITE"]


def computercolor():
    computercolorlist = []
    counter = 1
    while counter <= 4:
        colourchosen = random.choice(colourlist)
        computercolorlist.append(colourchosen)
        counter += 1
    print(computercolorlist)  #####################
    return computercolorlist


## error here if got duplicate values
def checkcolors(usercolorlist, computercolorlist):
    correctcolor = 0
    correctplace = 0
    allcorrect = 0
    colorindex = 0
    existcolor = []
    for element in usercolorlist:
        if element == computercolorlist[colorindex]:
            correctplace += 1
            existcolor.append(element)
        elif element != computercolorlist[colorindex] and element in computercolorlist:
            correctcolor += 1
        elif element != computercolorlist[colorindex] and element in computercolorlist and element in existcolor:
            correctcolor -= 1
        colorindex += 1

    if correctplace == 4:
        allcorrect = 1

    return correctcolor, correctplace, allcorrect


def usercolor(username):
    computercolorlist = computercolor()
    usercolorlist = []
    print(f"Welcome {username}! Let the games begin!\nHere are the colours for you to choose from:")
    c_num = 1
    tries = 1
    tryinfo = ""
    while True:
        os.system('cls')
        number = 0
        for colour in colourlist:
            print(f"{number} : {colour}")
            number += 1
        while c_num <= 4:
            colourchoices = input(f"Enter a colour's number to choose for colour slot {c_num}: ")
            try:
                colourchoices = int(colourchoices)
            except ValueError:
                print("Invalid input. Try again.")
                continue

            if 0 <= colourchoices <= len(colourlist):
                usercolorlist.append(colourlist[colourchoices])
                c_num += 1
            else:
                print("Enter a valid value!!!")
                continue

        print(f"Your colour selection as shown: {usercolorlist}")
        print("Processing......")
        time.sleep(1.5)
        correctcolor, correctplace, allcorrect = checkcolors(usercolorlist, computercolorlist)
        #correctcolor, correctplace, allcorrect = usercolorlist and computercolorlist in checkcolors
        print("Done!")
        if allcorrect == 0:
            tryinfo += f"{usercolorlist}, {correctcolor} correct color(s) but in wrong place, {correctplace} correct color in correct place(s)\n"
            print(tryinfo)
            print(
                f"This time, you got {correctcolor} correct colors but wrong place.\nYou also got {correctplace} correct placings.")
            print("Try again.")
            tries += 1
            c_num = 1
            usercolorlist = []
            continue
        else:
            os.system('cls')
            file_fh = open("guess_history.txt", "a")
            file_fh.write(f"{username},{tries},{datetime.datetime.now()}\n")
            file_fh.close()
            print(
                f"Congratulations! You got the combination correct :D\nThe combination is: {computercolorlist}\nTime completed: {datetime.datetime.now()}\nTotal tries: {tries}\nGet good noob.")
            while True:
                choice = input("[1]Play again\n[2]Exit the game\nEnter choice: ")
                if choice == "1":
                    return
                elif choice == "2":
                    print("Ok bye.")
                    exit()
                else:
                    print("Invalid input.")
                    continue


def gamestart():
    time.sleep(1)
    print("Starting Game...\n")
    time.sleep(1)
    while True:
        username = input("Enter a unique gamertag for yourself: ")

        if "," in username or username.strip() == "":
            print("Don't even try.")
            continue
        else:
            print(f"Your are: {username}, well of course you could've chosen a better gamertag.")
            while True:
                somechoice = input(
                    f"[1]Continue as {username}\n[2]Choose a different gamertag\n[3]Give up\nEnter your choice: ")
                if somechoice == '1':
                    usercolor(username)
                elif somechoice == '2':
                    break
                elif somechoice == "3":
                    print("Ok bye.")
                    return
                else:
                    print("Invalid input.")
                    continue
            continue


def guesshistory():
    showhistory = open("guess_history.txt", "r")
    counter = 0
    for line in showhistory:
        line_list = line.strip().split(",")
        dateplayed = datetime.datetime.strptime(line_list[2], "%Y-%m-%d %H:%M:%S.%f")
        print(f"Name: {line_list[0]}, Attempts: {line_list[1]}, Played on: {dateplayed}")
        counter += 1

    if counter == 0:
        print("No one has a record yet, set a world record yourself now!")
    else:
        print("END of Records~~~")


def gamerules():
    print("There are no rules.")


def gamescreen():
    os.system('cls')
    print("=======================================================")
    print("Welcome to the MasterMind game by Mannoj and gang")
    print("=======================================================")
    while True:
        print("Please select an option: ")
        print("[1] Read the rules and play the game")
        print("[2] Exit")
        print("[3] View everyone's Guessing History (BETA)")
        userchoice = input("Enter a selection (1-3): ")

        if userchoice == "1":
            print("Game start!")
            gamerules()
            gamestart()

        elif userchoice == "2":
            print("Ok bye.")
            exit()

        elif userchoice == "3":
            guesshistory()
            input("Enter anykey to continue: ")

        else:
            print("Choose a value between 1 to 3")
            continue

        continue


gamescreen()