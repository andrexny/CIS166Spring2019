# author: Andres Castillo
# module: lb-converter
# 4.29.19

from graphics import *

def main():
    winW, winH = 500,600
    winCenter = winW // 2
    win = GraphWin("Weight Converter", width=winW,height=winH)

    # create a user input box
    textEntry = Entry(Point(winCenter,150),10)
    textEntry.draw(win)

    messageText = Text(Point(winCenter,100),\
                       'Enter an amount in lbs.\n To quit, click on the window.')
    messageText.draw(win)

    fst = 50
    # init objects as empty so delete can happen first
    gramsOutput = Text(Point(winCenter,150+fst), "")
    gramsOutput.draw(win)
    kilogramsOutput = Text(Point(winCenter,200+fst), "")
    kilogramsOutput.draw(win)
    ouncesOutput = Text(Point(winCenter,250+fst), "")
    ouncesOutput.draw(win)

    skip = True

    lastString = ""
    while (win.checkMouse() == None):
        string = textEntry.getText()

        try:
            lb = float(string)
        except:
            lb = 0

        if string == lastString:
            continue;

        kilogramsOutput.undraw()
        gramsOutput.undraw()
        ouncesOutput.undraw()

        lastString = string
        grams = lb * 453.59237
        kilograms = lb * 0.45359237
        ounces = lb * 16

        gramsOutput = Text(Point(winCenter,150+fst), "grams: \n" + str(grams))
        gramsOutput.draw(win)
        kilogramsOutput = Text(Point(winCenter,200+fst), "kilograms: \n" + str(kilograms))
        kilogramsOutput.draw(win)
        ouncesOutput = Text(Point(winCenter,250+fst), "ounces: \n" + str(ounces))
        ouncesOutput.draw(win)
        time.sleep(.25)

main()
