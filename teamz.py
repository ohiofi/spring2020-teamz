
     _        _   _   _                               
  __| |_ _  _| |_| |_| |___   ___ _____ __ _ _ __ ___ 
 (_-| ' | || |  _|  _| / -_) / -_(_-/ _/ _` | '_ / -_)
 /__|_||_\_,_|\__|\__|_\___| \___/__\__\__,_| .__\___|
                                            |_|       

from time import *
from random import *

roomArray = []
for i in range(999):
   roomArray.append(False)

#kitchen
roomArray[304] = "You look out the window and see the beautiful planet Earth. The window seems like it was recently cleaned..."
roomArray[403] = "You enter the kitchen and check the sink. It seems there are some dishes that need to be put back..."
roomArray[404] = "To your west is a window freshly cleaned. East is a long hall. North is the kitchen, and south is the dining room."
roomArray[405] = "You walk into the dining room. It seems a fellow astronaut left something of theirs."

#bedrooms
roomArray[505] = "You have reached the workout room, here lies a treadmill for the astronauts to workout and stay fit /nto the west is the kitchen, to the north you hear creeking, south and east are the walls to you ship."
roomArray[504] = "This is the hallway... east you here snoring, to the west you hear a windex bottle, to the south you hear a treadmill."
roomArray[604] = "To the north the snoring increases, to the east you hear a flush, to the west the windex bottle sound grows lighter and to the south you see a window looking down to the earth."
roomArray[603] = "You have now reached the bedrooms... there is many clues here to help you escape /nTo the south is the hallway and to the west, east, and north are walls."

#hallway
roomArray[704] = "You smell something awful further down the hallway to the east, to the west you hear a quiet spraying sound."
roomArray[804] = "On the floor you see a towel with something brown on it, theres a door with a man and a women drawing on it to the south and walls to the east and north."
roomArray[805] = "You see a flouding toilet the awful smell is coming from the toilet and there are brown moist mushy bits of feces you notice something in the toilet. to the east is a air sealed door."
roomArray[905] = "Theres a door east it seems to be locked but you can see outside to outerspace."

def doesRoomExist(roomNumber):
    try:
        if roomArray(roomNumber) == False:
        print("you can not go there!")
            return False
        else:
            return True
    except:
        print("you can not go there")
        return False 
   
 def move(userInput, location):
    if userInput == "n" and doesRoomExist(location) == True:
        location = location - 1
    elif userInput == "s" and doesRoomExist(location)== True:
        location = location + 1
    elif userInput == "e" and doesRoomExist(location) == True:
        location = location + 100
    elif userInput == "w" and doesRoomExist(location) == True:
        location = location - 100
        return location
   
   def main():
    location = 404
    print("shuttle escape \nBy Matthew, Zach, Haydon")
    sleep(1)
    while True:
        print(roomArray[])
      if location == roomArray[304]:
        print("Item: Windex bottle")

    if location == roomArray[403]:
        print("Item: Spoon")

    if location == roomArray[405]:
        print("Item: Space suit")

    if location == roomArray[603]:
        print("Item: Key")

    if location == roomArray[505]:
        print("Item: Oxygen tank")

    if location == roomArray[805]:
        print("Item: Parachute")
    return location
        print("please type: n, s, e, w or quit ")
        userInput = input(userInput)
        location = move(userInput, location)
        break 
