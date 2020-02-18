from time import *
from random import *
from map import *

itemArray = []
roomArray = []
for i in range(999):
   roomArray.append(False)
   itemArray.append(False)

#items
itemArray[304] = "Windex bottle"
itemArray[403] = "Spoon"
itemArray[405] = "Space Suit"
itemArray[603] = "Key"
itemArray[505] = "Oxygen tank"
itemArray[805] = "Parachute"
itemArray[606] = "Router"
itemArray[607] = "Chickie Nuggies"
itemArray[507] = "A computer with Overwatch on it"
itemArray[707] = "Pizza"
itemArray[408] = "Gfuel"
itemArray[608] = "Yoda"
hasKey = False
inventory = []

#kitchen
roomArray[304] = "You look out the window and see the beautiful planet Earth. The window seems like it was recently cleaned..."
roomArray[403] = "You enter the kitchen and check the sink. It seems there are some dishes that need to be put back..."
roomArray[404] = "To your west is a window freshly cleaned. East is a long hall. North is the kitchen, and south is the dining room."
roomArray[405] = "You walk into the dining room. It seems a fellow astronaut left something of theirs."
roomArray[408] = "you see a man snorting something but he quickly hides it behind his back to you south, east, and west are walls."
roomArray[407] = "you here the snorting sound grow louder from the south to your north and west are walls."

#bedrooms
roomArray[507] = "you see a running computer with a game window open to your west you faintly hear snorting to your north and south are walls."
roomArray[505] = "You have reached the workout room, here lies a treadmill for the astronauts to workout and stay fit /nto the west is the kitchen, to the north you hear creeking, south and east are the walls to you ship."
roomArray[504] = "This is the hallway... east you here snoring, to the west you hear a windex bottle, to the south you hear a treadmill."
roomArray[604] = "To the north the snoring increases, to the east you hear a flush, to the west the windex bottle sound grows lighter and to the south you see a window looking down to the earth."
roomArray[603] = "You have now reached the bedrooms... there is many clues here to help you escape /nTo the south is the hallway and to the west, east, and north are walls."
roomArray[605] = "Here is the hallway that leads to the secod part of the station... \nto your east is the workout room and to your south you see the server room..."
roomArray[606] = "You have reached the router room. To south you smell the sweet smell of deep fried, bagged chicken nuggets"
roomArray[607] = "you have reached the secondary kitchen, to your south you see a mysterious locked room..."

#hallway
roomArray[704] = "You smell something awful further down the hallway to the east, to the west you hear a quiet spraying sound."
roomArray[707] = "you have reached the room of pizza... to your west you smell a great smell"
roomArray[804] = "On the floor you see a towel with something brown on it, theres a door with a man and a women drawing on it to the south and walls to the east and north."
roomArray[807] = "youve entered a room of nothingness... to your west you smell a delightful smell"
roomArray[805] = "You see a flouding toilet the awful smell is coming from the toilet and there are brown moist mushy bits of feces you notice something in the toilet. to the east is a air sealed door."
roomArray[905] = "Theres a door east it seems to be locked but you can see outside to outerspace."


def doesRoomExist(roomNumber):
    try:
        if roomArray[roomNumber] == False:
            print("you can not go there!")
            return False
        else:
            return True
    except:
        print("you can not go there")
        return False

def move(userInput, location):
    if userInput == "n" and doesRoomExist(location - 1) == True:
        location = location - 1
    elif userInput == "s" and doesRoomExist(location + 1)== True:
        location = location + 1
    elif userInput == "e" and doesRoomExist(location + 100) == True:
        location = location + 100
    elif userInput == "w" and doesRoomExist(location - 100) == True:
        location = location - 100
    return location

def main():
    map = Map()
    location = 404
    print("         ▄▄▄▄▄▄▄▄▄▄▄ ▄         ▄ ▄         ▄ ▄▄▄▄▄▄▄▄▄▄▄ ▄▄▄▄▄▄▄▄▄▄▄ ▄           ▄▄▄▄▄▄▄▄▄▄▄")
    sleep(0.25)
    print("        ▐░░░░░░░░░░░▐░▌       ▐░▐░▌       ▐░▐░░░░░░░░░░░▐░░░░░░░░░░░▐░▌         ▐░░░░░░░░░░░▌")
    sleep(0.25)
    print("        ▐░█▀▀▀▀▀▀▀▀▀▐░▌       ▐░▐░▌       ▐░▌▀▀▀▀█░█▀▀▀▀ ▀▀▀▀█░█▀▀▀▀▐░▌         ▐░█▀▀▀▀▀▀▀▀▀ ")
    #print("        ▐░▌         ▐░▌       ▐░▐░▌       ▐░▌    ▐░▌         ▐░▌    ▐░▌         ▐░▌             ")
    sleep(0.25)
    print("        ▐░█▄▄▄▄▄▄▄▄▄▐░█▄▄▄▄▄▄▄█░▐░▌       ▐░▌    ▐░▌         ▐░▌    ▐░▌         ▐░█▄▄▄▄▄▄▄▄▄      ")
    sleep(0.25)
    print("        ▐░░░░░░░░░░░▐░░░░░░░░░░░▐░▌       ▐░▌    ▐░▌         ▐░▌    ▐░▌         ▐░░░░░░░░░░░▌     ")
    sleep(0.25)
    print("         ▀▀▀▀▀▀▀▀▀█░▐░█▀▀▀▀▀▀▀█░▐░▌       ▐░▌    ▐░▌         ▐░▌    ▐░▌         ▐░█▀▀▀▀▀▀▀▀▀      ")
    #print("                  ▐░▐░▌       ▐░▐░▌       ▐░▌    ▐░▌         ▐░▌    ▐░▌         ▐░▌               ")
    sleep(0.25)
    print("         ▄▄▄▄▄▄▄▄▄█░▐░▌       ▐░▐░█▄▄▄▄▄▄▄█░▌    ▐░▌         ▐░▌    ▐░█▄▄▄▄▄▄▄▄▄▐░█▄▄▄▄▄▄▄▄▄      ")
    sleep(0.25)
    print("        ▐░░░░░░░░░░░▐░▌       ▐░▐░░░░░░░░░░░▌    ▐░▌         ▐░▌    ▐░░░░░░░░░░░▐░░░░░░░░░░░▌     ")
    sleep(0.25)
    print("         ▀▀▀▀▀▀▀▀▀▀▀ ▀         ▀ ▀▀▀▀▀▀▀▀▀▀▀      ▀           ▀      ▀▀▀▀▀▀▀▀▀▀▀ ▀▀▀▀▀▀▀▀▀▀▀      ")
    sleep(0.25)
    print("                                                                                                  ")
    sleep(1)
    print("              ▄▄▄▄▄▄▄▄▄▄▄ ▄▄▄▄▄▄▄▄▄▄▄ ▄▄▄▄▄▄▄▄▄▄▄ ▄▄▄▄▄▄▄▄▄▄▄ ▄▄▄▄▄▄▄▄▄▄▄ ▄▄▄▄▄▄▄▄▄▄▄             ")
    sleep(0.25)
    print("             ▐░░░░░░░░░░░▐░░░░░░░░░░░▐░░░░░░░░░░░▐░░░░░░░░░░░▐░░░░░░░░░░░▐░░░░░░░░░░░▌            ")
    sleep(0.25)
    print("             ▐░█▀▀▀▀▀▀▀▀▀▐░█▀▀▀▀▀▀▀▀▀▐░█▀▀▀▀▀▀▀▀▀▐░█▀▀▀▀▀▀▀█░▐░█▀▀▀▀▀▀▀█░▐░█▀▀▀▀▀▀▀▀▀             ")
    sleep(0.25)
    #print("             ▐░▌         ▐░▌         ▐░▌         ▐░▌       ▐░▐░▌       ▐░▐░▌                      ")
    print("             ▐░█▄▄▄▄▄▄▄▄▄▐░█▄▄▄▄▄▄▄▄▄▐░▌         ▐░█▄▄▄▄▄▄▄█░▐░█▄▄▄▄▄▄▄█░▐░█▄▄▄▄▄▄▄▄▄             ")
    sleep(0.25)
    print("             ▐░░░░░░░░░░░▐░░░░░░░░░░░▐░▌         ▐░░░░░░░░░░░▐░░░░░░░░░░░▐░░░░░░░░░░░▌            ")
    sleep(0.25)
    print("             ▐░█▀▀▀▀▀▀▀▀▀ ▀▀▀▀▀▀▀▀▀█░▐░▌         ▐░█▀▀▀▀▀▀▀█░▐░█▀▀▀▀▀▀▀▀▀▐░█▀▀▀▀▀▀▀▀▀             ")
    #print("             ▐░▌                   ▐░▐░▌         ▐░▌       ▐░▐░▌         ▐░▌                      ")
    print("             ▐░█▄▄▄▄▄▄▄▄▄ ▄▄▄▄▄▄▄▄▄█░▐░█▄▄▄▄▄▄▄▄▄▐░▌       ▐░▐░▌         ▐░█▄▄▄▄▄▄▄▄▄             ")
    sleep(0.25)
    print("             ▐░░░░░░░░░░░▐░░░░░░░░░░░▐░░░░░░░░░░░▐░▌       ▐░▐░▌         ▐░░░░░░░░░░░▌            ")
    sleep(0.25)
    print("              ▀▀▀▀▀▀▀▀▀▀▀ ▀▀▀▀▀▀▀▀▀▀▀ ▀▀▀▀▀▀▀▀▀▀▀ ▀         ▀ ▀           ▀▀▀▀▀▀▀▀▀▀▀       ")
    sleep(0.25)
    print("By Matthew, Zach, Haydon")
    sleep(1)
    while True:
        map.draw(roomArray, itemArray, location)
        print(str(roomArray[location]))
        if itemArray[location] != False:
            print("Item here: " + str(itemArray[location]))
            userInput = input("Please type: n, s, e, w, quit, or take: ")
            if userInput == "take":
                inventory.append(itemArray[location])
                itemArray[location] = False
                print(inventory)
                for each in inventory:
                    if each == "Key":
                        hasKey = True
                        roomArray[608] = "this was a very secret room... you have reached YODA!!! congrats on nothing"
        else:
            userInput = input("Please type: n, s, e, w or quit: ")
        if userInput == "quit":
            print("Thank you")
            break
        location = move(userInput, location)

#guessing game

def randomSecretWord():
    mylist1 = ["apple", "banana", "pear", "dragon fuit", "strawberry", "orange", "kiwi", "cucumber", "mango", "watermelon"]
    mylist2 = ["red", "yellow", "green",  "blue", "orange", "purple", "indigo", "maroon", "black", "white", "brown"]
    mylist3 = ["ohio", "texas", "kentucky", "california", "arkansas", "oklahoma", "iowa", "idaho", "alabama", "alaska"]
    combinedList = mylist1 + mylist2 + mylist3
    word = choice(combinedList)
    return word

def guessingGame():
    word = randomSecretWord()
    word = word.lower()
    print("I'm thinking of a secret word. Take a guess between fruits, colors, and state names and you may be able to unlock the doors... ")
    while True:
        print("guess a word")
        userInput = input()
        userInput = userInput.lower()
        if userInput < word:
            print("The secret word is after " + userInput)
        if userInput > word:
            print("the secret word is before " + userInput)
        if userInput == word:
            print("you got it!")
            break

#OverWatch MiniGame
def owMiniGame(questionText):
    while True:
        answer = input()
        answer = int(answer)
        if answer == 2016:
            print("congrats! a mysterious password of sorts shows on the screen Password: ooga booga")
            break
        else:
            print("try again")
