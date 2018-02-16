from graphics import *

# Constants

PATCH_PIXEL = 100  # The size of each patch in pixels
COORD_SCALE = 10  # How much to scale the coordinates down by

PATCH_SIZE = PATCH_PIXEL//COORD_SCALE  # The patch size after coord re-mapping

# Helper Functions


def drawRectangle(win, lengthX, lengthY, point, colour="", outline="black"):
    rectangle = Rectangle(point, Point(point.getX() + lengthX,
                          point.getY() + lengthY))
    rectangle.setFill(colour)
    rectangle.setOutline(outline)
    rectangle.draw(win)
    return rectangle


def drawPolygon(win, points, colour="", outline=""):
    polygon = Polygon(points)
    polygon.setFill(colour)
    polygon.setOutline(outline)
    polygon.draw(win)
    return polygon


def drawLine(win, point1, point2, colour="black"):
    line = Line(point1, point2)
    line.setFill(colour)
    line.draw(win)
    return line

# Main Program Functions


def getInputs():
    size = 0
    while size == 0:
        sizeIn = input("How large should the square " +
                       "grid of patches be (5, 7, 9, 11)? ")
        if sizeIn in ["5", "7", "9", "11"]:
            size = int(sizeIn)
        else:
            print("The input must be one of 5, 7, 9 or 11!")
    colours = []
    validColours = ["red", "green", "blue", "magenta",
                    "cyan", "orange", "brown", "pink"]
    print("Choose three different colours for the patches, "
          "these can be any from: \n{}.".format(", ".join(validColours)))
    while len(colours) < 3:
        colourIn = input("What is colour #{}? "
                         .format(len(colours) + 1)).lower()
        if colourIn in validColours:
            if colourIn not in colours:
                colours.append(colourIn)
            else:
                print("The colour \"{}\" has already been used, pick another!"
                      .format(colourIn))
        else:
            print("\"{}\" is not a valid colour!".format(colourIn))
    return size, colours


def drawPatch1(win, x, y, colour):
    # The final patch (star)
    for edge in range(11):
        drawLine(win, Point(x + edge, y + 10), Point(x + 10 - edge, y), colour)
        drawLine(win, Point(x, y + 10 - edge), Point(x + 10, y + edge), colour)


def drawPatch2(win, x, y, colour):
    # The penultimate patch (zig-zags)
    for lineY in range(0, 9, 2):
        points = [0]*22
        # The list needs to be 22 long so values can be assigned backwards.
        for cornerX in range(11):
            offsetY = ((cornerX+1) % 2)
            upperPoint = Point(x + cornerX, y + offsetY + lineY)
            lowerPoint = Point(x + cornerX, y + offsetY + lineY + 1)
            points[cornerX], points[21-cornerX] = upperPoint, lowerPoint
        drawPolygon(win, points, colour)


def drawPatch(patch, win, x, y, colour):
    if patch:
        drawPatch2(win, x, y, colour)
    else:
        drawPatch1(win, x, y, colour)
    drawRectangle(win, PATCH_SIZE, PATCH_SIZE, Point(x, y))


def drawPatches(win, patchAmount, colours):
    patternGrid = []
    counter = 0
    for y in range(0, patchAmount*PATCH_SIZE, PATCH_SIZE):
        patternGrid.append([])
        for x in range(0, patchAmount*PATCH_SIZE, PATCH_SIZE):
            colour = colours[counter % len(colours)]
            drawPatch(x > y, win, x, y, colour)
            patternGrid[y//PATCH_SIZE].append((x > y, colour))
            counter += 1
            # Simple way to get a value increasing across both for loops
    return patternGrid

# Advanced Program Functions


def swapper(win, size, colours, patternGrid):
    while True:
        mouse1, mouse2 = win.getMouse(), win.getMouse()
        x1, y1 = int(mouse1.getX()//PATCH_SIZE), int(mouse1.getY()//PATCH_SIZE)
        x2, y2 = int(mouse2.getX()//PATCH_SIZE), int(mouse2.getY()//PATCH_SIZE)
        # These are the grid coordinates, ranging from 0 to patchAmount-1
        grid1 = patternGrid[y1][x1]
        grid2 = patternGrid[y2][x2]
        drawRectangle(win, PATCH_SIZE, PATCH_SIZE,
                      Point(x1*PATCH_SIZE, y1*PATCH_SIZE), "white", "")
        # Blank out the square first clicked in
        if x1 == x2 and y1 == y2:
            patternGrid[y1][x1] = (not grid1[0], grid1[1])
            drawPatch(not grid1[0], win, x1*PATCH_SIZE,
                      y1*PATCH_SIZE, grid1[1])
        else:
            drawRectangle(win, PATCH_SIZE, PATCH_SIZE,
                          Point(x2*PATCH_SIZE, y2*PATCH_SIZE), "white", "")
            # Blank out second square as that is now needed
            patternGrid[y1][x1], patternGrid[y2][x2] = grid2, grid1
            drawPatch(grid2[0], win, x1*PATCH_SIZE, y1*PATCH_SIZE, grid2[1])
            drawPatch(grid1[0], win, x2*PATCH_SIZE, y2*PATCH_SIZE, grid1[1])

# Main Function


def main():
    patchAmount, colours = getInputs()
    win = GraphWin("INTPROG Coursework 1", patchAmount*PATCH_PIXEL,
                   patchAmount*PATCH_PIXEL)
    win.setCoords(-0.2, patchAmount*COORD_SCALE - 0.2,
                  patchAmount*COORD_SCALE - 0.2, -0.2)
    # -0.2 to compensate for GraphWin border (only works at default scale)
    win.setBackground("white")
    patternGrid = drawPatches(win, patchAmount, colours)
    swapper(win, patchAmount, colours, patternGrid)

main()
