from time import *
from random import *

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

#kitchen
roomArray[304] = "You look out the window and see the beautiful planet Earth. The window seems like it was recently cleaned..."
roomArray[403] = "You enter the kitchen and check the sink. It seems there are some dishes that need to be put back..."
roomArray[404] = "To your west is a window freshly cleaned. East is a long hall. North is the kitchen, and south is the dining room."
roomArray[405] = "You walk into the dining room. It seems a fellow astronaut left something of theirs."

#bedrooms
roomArray[505] = "You have reached the workout room, here lies a treadmill for the astronauts to workout and stay fit \nto the west is the kitchen, to the north you hear creeking, south and east are the walls to you ship."
roomArray[504] = "This is the hallway... east you here snoring, to the west you hear a windex bottle, to the south you hear a treadmill."
roomArray[604] = "To the north the snoring increases, to the east you hear a flush, to the west the windex bottle sound grows lighter and to the south you see a window looking down to the earth."
roomArray[603] = "You have now reached the bedrooms... there is many clues here to help you escape \nTo the south is the hallway and to the west, east, and north are walls."

#hallway
roomArray[704] = "You smell something awful further down the hallway to the east, to the west you hear a quiet spraying sound."
roomArray[804] = "On the floor you see a towel with something brown on it, theres a door with a man and a women drawing on it to the south and walls to the east and north."
roomArray[805] = "You see a flouding toilet the awful smell is coming from the toilet and there are brown moist mushy bits of feces you notice something in the toilet. to the east is a air sealed door."
roomArray[905] = "Theres a door east it seems to be locked but you can see outside to outerspace."

# Mr. Riley's map class v1.90208
#
# How to use Mr. Riley's map class...
# 1.) from map import *
# 2.) create a map instance: map = Map()
# 3.) draw/redraw the map inside the game loop: map.draw(roomList, itemList, currentlocation)
# Don't wanna show yer item locations? Do this: map.draw(roomList, False, currentlocation)

from turtle import *
from math import *
from map import *

map = Map()



class Map(Turtle):
    def __init__(self):
        Turtle.__init__(self)
        self.speed(0)
        self.penup()
        self.screen = Screen()
        self.size = 400  # map window size
        self.mapBorder = 20
        self.roomSize = 20
        self.roomBorder = 2
        self.startingLocation = None
        self.columnHeight = 100
        self.screen.setup(self.size, self.size)
        self.screen.tracer(0)
        self.screen.bgcolor("black")
        self.roomColor = "white"
        self.startTextColor = "green"
        self.bigStarColor = "blue"
        self.littleStarColor = "orange"
        self.screen.register_shape(
            "bigStar",
            (
            (-10, -6.5),
            (10, 0),
            (-10, 6.5),
            (2.5, -10),
            (2.5, 10),
            (-10, -6.5)
            ),
        )
        self.littleStarSize = 4
        self.screen.register_shape(
            "littleStar",
            (
                (-10 / self.littleStarSize, -6.5 / self.littleStarSize),
                (10 / self.littleStarSize, 0),
                (-10 / self.littleStarSize, 6.5 / self.littleStarSize),
                (2.5 / self.littleStarSize, -10 / self.littleStarSize),
                (2.5 / self.littleStarSize, 10 / self.littleStarSize),
                (-10 / self.littleStarSize, -6.5 / self.littleStarSize),
            ),
        )
        # reveal instance variables
        self.revealDistance = 2
        self.revealWallColor = "gray"
        self.mappedRooms = []
        self.mappedItems = []
        for i in range(1999):
            self.mappedRooms.append(None)
            self.mappedItems.append(False)

    def setBackgroundColor(self, color="black"):
        self.screen.bgcolor(color)

    def setRoomColor(self, color="white"):
        self.roomColor = color

    def setRevealWallColor(self, color="gray"):
        self.revealWallColor = color

    def setBigStarColor(self, color="red"):
        self.bigStarColor = color

    def setLittleStarColor(self, color="gold"):
        self.littleStarColor = color

    def setTextColor(self, color):
        self.startTextColor = color

    # if there is no starting location, set it
    def setStartingLocation(self, myLocation):
        if self.startingLocation is None:
            self.startingLocation = myLocation

    # transfer rooms within the reveal distance from the rooms array to the mapped rooms array
    def mapTheSurroundingArea(self, myLocation, rooms, roomItems):
        for row in range(
            myLocation % self.columnHeight - self.revealDistance,
            myLocation % self.columnHeight + self.revealDistance + 1,
        ):
            for col in range(
                myLocation // self.columnHeight * self.columnHeight
                - self.revealDistance * self.columnHeight,
                myLocation // self.columnHeight * self.columnHeight
                + self.revealDistance * self.columnHeight
                + self.columnHeight,
                self.columnHeight,
            ):
                try:
                    self.mappedRooms[row + col] = rooms[row + col]
                    self.mappedItems[row + col] = roomItems[row + col]
                except:
                    pass

    # if there is a room here, stamp a square at the current row and column
    def drawRoom(self, row, column, roomArray):
        try:
            if roomArray[column * self.columnHeight + row]:
                self.color(self.roomColor)
                self.shape("square")
                self.goto(
                    -self.size / 2
                    + (self.roomSize / 2)
                    + column * (self.roomSize + self.roomBorder)
                    + self.mapBorder,
                    self.size / 2
                    - (self.roomSize / 2)
                    - row * (self.roomSize + self.roomBorder)
                    - self.mapBorder,
                )
                self.stamp()
        except:
            pass

    # if there is a revealed wall here, stamp a square at the current row and column
    def drawRevealedWall(self, row, column, roomArray):
        try:
            if roomArray[column * self.columnHeight + row] is False:
                self.color(self.revealWallColor)
                self.shape("square")
                self.goto(
                    -self.size / 2
                    + (self.roomSize / 2)
                    + column * (self.roomSize + self.roomBorder)
                    + self.mapBorder,
                    self.size / 2
                    - (self.roomSize / 2)
                    - row * (self.roomSize + self.roomBorder)
                    - self.mapBorder,
                )
                self.stamp()
        except:
            pass

    # if there is an item here, stamp a little star at the current row and column
    def drawLittleStar(self, row, column, itemArray):
        try:
            if itemArray[column * self.columnHeight + row]:
                self.color(self.littleStarColor)
                self.shape("littleStar")
                # self.goto(-self.size/2+(self.roomSize/2)+column*(self.roomSize+self.roomBorder)+self.mapBorder,self.size/2-(self.roomSize/2)-row*(self.roomSize+self.roomBorder)-self.mapBorder)
                self.stamp()
        except:
            pass

    # if there the startingLocation is here, write Start at the current row and column
    def drawStart(self, row, column, _startingLocation):
        if _startingLocation == column * self.columnHeight + row:
            self.color(self.startTextColor)
            self.back(self.roomSize / 2)
            self.write("Start", font=("Arial", 7, "normal"))
            self.forward(self.roomSize / 2)

    # if the currentlocation is here, stamp a big star at the current row and column
    def drawBigStar(self, row, column, myLocation):
        if myLocation == column * self.columnHeight + row:
            self.color(self.bigStarColor)
            self.shape("bigStar")
            self.stamp()

    # use the draw method to draw and redraw the map
    def draw(self, rooms, roomItems, myLocation):
        rowWidth = int(math.ceil(len(rooms) / self.columnHeight))
        self.penup()
        self.clear()
        self.setStartingLocation(myLocation)
        for row in range(self.columnHeight):
            for column in range(rowWidth):
                self.drawRoom(row, column, rooms)
                self.drawLittleStar(row, column, roomItems)
                self.drawStart(row, column, self.startingLocation)
                self.drawBigStar(row, column, myLocation)
        self.screen.update()

    # use the reveal method (instead of draw) to SLOWLY draw and reveal the map
    def reveal(self, rooms, roomItems, myLocation):
        self.mapTheSurroundingArea(myLocation, rooms, roomItems)
        rowWidth = int(math.ceil(len(rooms) / self.columnHeight))
        self.penup()
        self.clear()
        self.setStartingLocation(myLocation)
        for row in range(self.columnHeight):
            for column in range(rowWidth):
                self.drawRoom(row, column, self.mappedRooms)
                self.drawRevealedWall(row, column, self.mappedRooms)
                self.drawLittleStar(row, column, self.mappedItems)
                self.drawStart(row, column, self.startingLocation)
                self.drawBigStar(row, column, myLocation)
        self.screen.update()

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
        print(str(roomArray[location]))
        if itemArray[location] != False:
            print("Item here: " + str(itemArray[location]))
            userInput = input("Please type: n, s, e, w, quit, or take: ")
        else:
            userInput = input("Please type: n, s, e, w or quit: ")
        if userInput == "quit":
            print("Thank you")
            break
        location = move(userInput, location)
