import random

def init():
    global variety
    variety = ["ko", "papir", "ollo"]
    menu()

def menu():
    try:
        userInput = int(input("Valassz:\n1 - ko\n2 - papir\n3 - ollo\n0 - kilepes"))
        if userInput == 1:
            game("ko", computerRandom())
        elif userInput == 2:
            game("papir", computerRandom())
        elif userInput == 3:
            game("ollo", computerRandom())
        elif userInput == 0:
            exit()
        else:
            menu()
    except:
        print("Szamot adj meg!")

def computerRandom():
    computerChoice = variety[random.randint(0,len(variety)-1)]
    print(f"A szamitogep valasza: {computerChoice}")
    return computerChoice

def game(userChoice, compCh):
    if userChoice == compCh:
        print("Dontetlen\n")
        menu()
    elif userChoice == "ko":
        if compCh == "papir":
            print(f"Vesztettel, a {compCh} uti a(z) {userChoice}-(ve)t\n")
            menu()
        elif compCh == "ollo":
            print(f"Nyertel, a {userChoice} uti a(z) {compCh}-(ve)t\n")
            menu()
    elif userChoice == "papir":
        if compCh == "ko":
            print(f"Nyertel, a {userChoice} uti a(z) {compCh}-(ve)t\n")
            menu()
        elif compCh == "ollo":
            print(f"Vesztettel, a {compCh} uti a(z) {userChoice}-(ve)t\n")
            menu()
    elif userChoice == "ollo":
        if compCh == "ko":
            print(f"Vesztettel, a {compCh} uti a(z) {userChoice}-(ve)t\n")
            menu()
        if compCh == "papir":
            print(f"Nyertel, a {userChoice} uti a(z) {compCh}-(ve)t\n")
            menu()
    else:
        print("Valami nem jo dolog tortent.")
        menu()

init()