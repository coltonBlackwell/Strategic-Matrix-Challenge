import datetime as dt
import random

from createGraphics import graphicGame

boards = {0: "boards/board0.csv", 1: "boards/board1.csv", 2: "boards/board2.csv", 3: "boards/board3.csv"}

x1 = [1, 2, 3]
y1 = [1, 2, 3]
secondsList2 = [1, 2, 3]


def createBoardList(boardName):
    reformedList = []

    with open(boardName, "r") as file:
        turns = file.readline()
        turns = turns[0]
        for row in file:
            line = row.strip().split(",")
            line = [int(i) for i in line]
            reformedList.append(line)
    return reformedList, int(turns)


def displayBoard(newElement):

    rowCounter = 0
    header = "\t\tColumn 0\tColumn 1\tColumn 2"
    if len(newElement) == 4:
        header += "\tColumn 3"
    print(header, "\n")
    for row in newElement:
        stringInts = [str(int) for int in row]
        stringOfInts = "\t\t\t".join(stringInts)
        print("Row", rowCounter, "\t\t", stringOfInts, "\n")
        rowCounter += 1


def changeValues(newElement, userRow, userColumn, userValue):

    newElement[userRow][userColumn] = str(userValue)
    displayBoard(newElement)


def computerTurn(newElement):
    randomRow = random.randint(1, 3)
    randomColumn = random.randint(0, 2)
    randomValue = random.randint(0, 50)
    y2.append(int(randomValue))
    newElement[randomRow][randomColumn] = str(randomValue)
    print(
        "(after computer played in (row,col):",
        (randomRow, randomColumn),
        "with value:",
        randomValue,
        ")\n",
    )
    displayBoard(newElement)


def calcPoints(newElement):

    evenCounter = 0
    for rows in newElement:
        for num in rows:
            if int(num) % 2 == 0 and int(num) != 99:
                evenCounter += int(num)

    a, b = createBoardList(boardName)

    finalPoints = evenCounter / b

    return int(finalPoints), evenCounter


def rowEvenOdd(newElement):
    emptyString = []
    isEven = True
    for rows in newElement:
        emptyValue = 0
        for num in rows:
            emptyValue += int(num)
        emptyString.append(emptyValue)

    for num in emptyString:
        if num % 2 != 0:
            isEven = False

    return isEven


def colEvenOdd(newElement):
    col1total = 0
    col2total = 0
    col3total = 0
    col4total = 0
    isOdd = True

    for rows in newElement:

        for i in range(len(rows)):
            col1total += int(newElement[i][0])
            col2total += int(newElement[i][1])
            col3total += int(newElement[i][2])
            if len(newElement) == 4:
                col4total += int(newElement[i][3])

        break
    totalList = [col1total, col2total, col3total]
    if len(newElement) == 4:
        totalList.append(col4total)

    for num in totalList:
        if num % 2 == 0:
            isOdd = False

    return isOdd


def resultEvenOdd(newElement):
    rowOutcome = rowEvenOdd(newElement)
    columnOutcome = colEvenOdd(newElement)
    gameOutcome = True

    if rowOutcome == False or columnOutcome == False:
        print("You Lose!!")
        gameOutcome = False

    else:
        print("You win!!")
    return gameOutcome


def calcGameSeconds(secondsList):
    totalValue = 0
    for num in secondsList:
        totalValue += num

    return totalValue


print("Dear player! Welcome to the 'Even/Odd Colourful Graphical' game")
print("=================================================\n")

print("With this system you will be able to play as many games as you want!")
print("The objective of this game is that rows in the board")
print("add to an even number and all columns in the board add to an odd number")
print("For each game: ")
print("\t-You will be able to choose to play 'SOLO' or against the computer ('AI')")
print("\t-You will be able to choose an initial board")
print("\t-At the end of each game you will win (or lose) points")
print("\t-You will see a graphical representation of some game related values.\n\n")

userPlay = "y"

gameNumber = 0

totalPoints = 0

gamesWon = 0


while userPlay == "y":
    userPlay = input("Would you like to play (y/n)?").lower()

    if userPlay == "y":
        gameNumber += 1
        x2 = []
        y2 = []
        secondsList = []
        maxNum = "2"

        print("\n\nGame:", gameNumber)
        print("=========\n\n")

        gameStyle = input(
            "Which style would you like to play ('SOLO or 'AI'): ==> "
        ).upper()


        userBoard = int(
          input("\nWhich intital board do you want to use? (0,1,2,3) ==> ")
        )


        if userBoard == 2 or userBoard == 3:
            x1 = [1, 2, 3, 4]
            y1 = [1, 2, 3, 4]
            secondsList2 = [1, 2, 3, 4]

        if userBoard == 2 or userBoard == 3:
            maxNum = "3"
        boardName = boards[userBoard]
        newElement, turns = createBoardList(boardName)

        print("\n\nThe board is")
        print("------------\n")
        print("(initial board)\n")
        displayBoard(newElement)
        print("------------\n")
        for i in range(turns):
            now1 = dt.datetime.now()
            print("You have", turns, "turns left...\n")
            print("User, where do you want your value? (row 99 - no more turns)\n")
            userRow = int(input("row?  (>=0 and <= {}) ==> ".format(maxNum)))
            if userRow == 99:
                print(
                    "Since you didn't want to update more values, the game is over..."
                )
                turns = 0
                break
            userColumn = int(input("column?  (>=0 and <= {}) ==> ".format(maxNum)))
            userValue = int(input("value (0 to 50): ==> "))
            x2.append(userValue)
            print("The board is")
            print("-----------------------")
            print("(after user played)\n")
            changeValues(newElement, userRow, userColumn, userValue)
            print("-----------------------")

            if gameStyle == "AI":
                computerTurn(newElement)

            now2 = dt.datetime.now()

            diff_in_secs = (now2 - now1).total_seconds()

            secondsList.append(int(diff_in_secs))

            turns -= 1

        print("You reached the maximum turns possible, the game is over!")
        print("Totals for this game")
        print("------------------\n\n")
        pointValue, evenCount = calcPoints(newElement)

        rowEvenOdd(newElement)
        colEvenOdd(newElement)
        resultEvenOdd(newElement)
        print("The points resulting from this game are:", pointValue)
        print("Points are calculated as:")
        print("   The sum of all even values in the board", evenCount)
        print("   divided by the number of turns played", (4))

        gameDecider = resultEvenOdd(newElement)
        print("----------------\n")
        if gameDecider == True:
            print("Yey! User, you won this game!")
            print("All rows add to even numbers and all cols add to odd numbers!")
            print("You will be added", pointValue, "to your total")
            totalPoints += pointValue
            gamesWon += 1
        else:
            print("So sorry, User, you lost this game!")
            print(
                "Not all rows add to even numbers or not all cols add to odd numbers!"
            )
            print("You will be subtracted", pointValue, "points from your total...")
            totalPoints -= pointValue
        print("Your points so far are:", totalPoints, "\n\n")
        print("(SEE GRAPHIC GAME)")
        print("Seconds each turn", secondsList)
        print("User values each turn", x2)

        if gameStyle == "AI":
            print("AI values each turn", y2)

        graphicGame(x1, x2, y1, y2, secondsList2, secondsList, gameNumber, gameStyle)

    elif userPlay == "n":
        print("Thanks for playing!")
        break
    else:
        print("Please either input y (yes) or n (no) into the prompt!\n\n")
        userPlay = "y"

print("\n****************\n\n")
print("TOTALS ALL GAMES")
print("User's total points in all games:", totalPoints)
print("Total games the User won: ", gamesWon)
