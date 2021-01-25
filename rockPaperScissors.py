import random

def win(userWin):
    if userWin == True:
        print("\n\n\n\nGratulalok, legyozted a szamitogepet!\n\n")
        reset()
    else:
        print("\n\n\n\nNe csuggedj, mosz kikaptal a szamitogeptol, de legkozelebb biztosan nagyobb szerencsed lesz!\n\n")
        reset()

def init():
    global variety
    variety = ["ko", "papir", "ollo"]
    reset()

def reset():
    userPoints = 0
    computerPoints = 0
    menu(userPoints, computerPoints, howManyPointsToWin())

def howManyPointsToWin():
    try:
        userInput = int(input("Ird be, hogy hany pont kelljen a gyozelemhez 1 es 10 kozott. 1 nyert kor = 1 pont. : "))
        if userInput > 10:
            print("A megadott szam nagyobb mint 10. Adj meg a meghatarozott erteken beluli szamot!")
            return howManyPointsToWin()
        elif userInput < 1:
            print("A megadott szam kisebb mint 1. Adj meg a meghatarozott erteken beluli szamot!")
            return howManyPointsToWin()
        else:
            print(f"{userInput} pont kell a gyozelemhez!")
            return(userInput)
    except:
        print("Ervenyes szamot adj meg!")
        return howManyPointsToWin()

def pointChecker(uP, cP, ptw): #uP = userPoints, cP = computerPoints, ptw = points to win
    if uP == ptw:
        win(True)
    elif cP == ptw:
        win(False)
    else:
        menu(uP, cP, ptw)


def pointAdder(playerWon, uP, cP, ptw): #uP = userPoints, cP = computerPoints, ptw = points to win
    if playerWon == True:
        uP = uP + 1
        pointChecker(uP, cP, ptw)
    else:
        cP = cP + 1
        pointChecker(uP, cP, ptw)

def menu(userPoints, computerPoints, ptw): #ptw = points to win
    try:
        userInput = int(input("Valassz:\n1 - ko\n2 - papir\n3 - ollo\n0 - kilepes"))
        if userInput == 1:
            game("ko", computerRandom(), userPoints, computerPoints, ptw)
        elif userInput == 2:
            game("papir", computerRandom(), userPoints, computerPoints, ptw)
        elif userInput == 3:
            game("ollo", computerRandom(), userPoints, computerPoints, ptw)
        elif userInput == 0:
            exit()
        else:
            menu(userPoints, computerPoints, ptw)
    except:
        print("Szamot adj meg!")

def computerRandom():
    computerChoice = variety[random.randint(0,len(variety)-1)]
    print(f"A szamitogep valasza: {computerChoice}")
    return computerChoice

def game(userChoice, compCh, userPoints, computerPoints, ptw): #ptw = points to win
    if userChoice == compCh:
        print("Dontetlen\n")
        menu(userPoints, computerPoints, ptw)
    elif userChoice == "ko":
        if compCh == "papir":
            print(f"Vesztettel, a {compCh} uti a(z) {userChoice}-(ve)t\n")
            pointAdder(False, userPoints, computerPoints, ptw)
        elif compCh == "ollo":
            print(f"Nyertel, a {userChoice} uti a(z) {compCh}-(ve)t\n")
            pointAdder(True, userPoints, computerPoints, ptw)
    elif userChoice == "papir":
        if compCh == "ko":
            print(f"Nyertel, a {userChoice} uti a(z) {compCh}-(ve)t\n")
            pointAdder(True, userPoints, computerPoints, ptw)
        elif compCh == "ollo":
            print(f"Vesztettel, a {compCh} uti a(z) {userChoice}-(ve)t\n")
            pointAdder(False, userPoints, computerPoints, ptw)
    elif userChoice == "ollo":
        if compCh == "ko":
            print(f"Vesztettel, a {compCh} uti a(z) {userChoice}-(ve)t\n")
            pointAdder(False, userPoints, computerPoints, ptw)
        if compCh == "papir":
            print(f"Nyertel, a {userChoice} uti a(z) {compCh}-(ve)t\n")
            pointAdder(True, userPoints, computerPoints, ptw)

init()
