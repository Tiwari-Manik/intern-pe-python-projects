import random

print("Welcome to Connect Four")
print("-----------------------")

possibleLetters = ["A", "B", "C", "D", "E", "F", "G"]
gameBoard = [["" for _ in range(7)] for _ in range(6)]
rows = 6
cols = 7

def printGameBoard():
    print("\n     A    B    C    D    E    F    G  ", end="")
    for x in range(rows):
        print("\n   +----+----+----+----+----+----+----+")
        print(x, " |", end="")
        for y in range(cols):
            if gameBoard[x][y] == "🔵":
                print("", gameBoard[x][y], end=" |")
            elif gameBoard[x][y] == "🔴":
                print("", gameBoard[x][y], end=" |")
            else:
                print(" ", gameBoard[x][y], end="  |")
    print("\n   +----+----+----+----+----+----+----+")

def modifyTurn(column, turn):
    for row in range(rows-1, -1, -1):
        if gameBoard[row][column] == "":
            gameBoard[row][column] = turn
            return True
    return False

def checkWin(turn):
    # Check horizontal locations for win
    for row in range(rows):
        for col in range(cols-3):
            if gameBoard[row][col] == turn and gameBoard[row][col+1] == turn and gameBoard[row][col+2] == turn and gameBoard[row][col+3] == turn:
                return True

    # Check vertical locations for win
    for row in range(rows-3):
        for col in range(cols):
            if gameBoard[row][col] == turn and gameBoard[row+1][col] == turn and gameBoard[row+2][col] == turn and gameBoard[row+3][col] == turn:
                return True

    # Check positively sloped diagonals
    for row in range(rows-3):
        for col in range(cols-3):
            if gameBoard[row][col] == turn and gameBoard[row+1][col+1] == turn and gameBoard[row+2][col+2] == turn and gameBoard[row+3][col+3] == turn:
                return True

    # Check negatively sloped diagonals
    for row in range(3, rows):
        for col in range(cols-3):
            if gameBoard[row][col] == turn and gameBoard[row-1][col+1] == turn and gameBoard[row-2][col+2] == turn and gameBoard[row-3][col+3] == turn:
                return True

    return False

turnCounter = 0
while True:
    printGameBoard()
    if turnCounter % 2 == 0:
        turn = "🔴"
    else:
        turn = "🔵"
    
    while True:
        colPick = input(f"\nPlayer {turn}, choose a column (A-G): ").upper()
        if colPick in possibleLetters:
            colIndex = possibleLetters.index(colPick)
            if modifyTurn(colIndex, turn):
                break
            else:
                print("Column is full, choose another one.")
        else:
            print("Invalid column. Please choose between A and G.")

    if checkWin(turn):
        printGameBoard()
        print(f"\nPlayer {turn} wins!")
        break

    turnCounter += 1

    if turnCounter == rows * cols:
        printGameBoard()
        print("\nIt's a tie!")
        break