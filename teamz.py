from time import *
from random import *

roomArray = []
for i in range(999):
   roomArray.append(False)

#kitchen
    
#bedrooms
roomArray[505] = ("you have reached the workout room, here lies a treadmill for the astronauts to workout and stay fit /nto the west is the kitchen, to the north you hear creeking, south and east are the walls to you ship")
roomArray[504] = ("this is the hallway... /neast you here snoring, to the west you hear a windex bottle, to the south you hear a treadmill") 
roomArray[604] = ("to the north the snoring increases, to the east you hear a flush, to the west the windex bottle sound grows lighter and to the south you see a window looking down to the earth")
roomArray[603] = ("you have now reached the bedrooms... there is many clues here to help you escape /nTo the south is the hallway and to the west, east, and north are walls")

#hallway
roomArray[704] = "you smell something awful further down the hallway to the east, to the west you hear a quiet spraying sound."
roomArray[804] = "on the floor you see a towel with something brown on it, theres a door with a man and a women drawing on it to the south and walls to the east and north."
roomArray[805] = "you see a flouding toilet the awful smell is coming from the toilet and there are brown moist mushy bits of feces you notice something in the toilet. to the east is a air sealed door."
roomArray[905] = "theres a door east it seems to be locked but you can see outside to outerspace."







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
        print("please type: n, s, e, w or quit ")
        userInput = input(userInput)
        location = move(userInput, location)
        break 
