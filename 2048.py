import random
import copy
boardSize = 4

def display():
    largest = board[0][0]
    for row in board:
        for element in row:
            if element > largest:
                largest = element
                
numSpaces = len(str(largest))

for row in board:
    currRow = "|"
    for element in row:
        if element == 0:
           currRow += " " * numSpaces + "|"
        else:
         currrow += (" " * (numSpaces - len(str(element)))) + str(element) + "|"
            
    print(currRow)
print() 
display()
    
def mergeOneRowL(row):
        
    for j in range(boardSize - 1):
        for i in range(boardSize - 1, 0, -1):
            
            if row[i - 1] == 0:
                row[i - 1] = row[i]
                row[i] = 0
                
        
    for i in range(boardSize - 1):
        if row[i] == row[i + 1]:
            row[i] *= 2
            row[i + 1] = 0
            
            
        for i in range(boardSize - 1, 0, -1):
            if row[i - 1] == 0:
                row[i - 1] = row[i]
                row[i] = 0
                
            return row
    
    def merge_left(currentBoard):
        for i in range(boardSize):
            currentBoard[i] = mergeOneRowL(currentBoard[i])
            
    return currentBoard

    
    def reverse(row):
        new = []
        for i in range(boardSize - 1, -1, -1):
            new.append(row[i])
            return new
        
    def merge_right(currentBoard):
        
        for i in range(boardSize):
            
         currentBoard[i] = reverse(currentBoard[i])
         currentBoard[i] = mergeOneRowL(currentBoard[i])
         currentBoard[i] = reverse(currentBoard[i])
        
        return currentBoard
    
    def transpose(currentBoard):
        for j in range(boardSize):
            for i in range(j, boardSize):
                if not i == j:
                    temp = currentBoard[j][i]
                    currentBoard[j][i] = currentBoard[i][j]
                    currentBoard[i][j] = temp
        return currentBoard
    
    def merge_up(currentBoard):
        
        currentBoard = transpose(currentBoard)
        currentBoard = merge_left(curentBoard)
        currentBoard = transpose(currentBoard)
        
        return currentBoard
    
    def merge_down(currentBoard):
        
        currentBoard = transpose(currentBoard)
        currentBoard = merge_right(currentBoard)
        currentBoard = transpose(currentBoard)
        
        return currentBoard
    
    def pickNewValue():
        if random.randint(1, 8) == 1:
            return 4
        else:
            return 2
        
        def addNewValue():
            rowNum = random.randint(0, boardSize - 1)
            colNum = random.randint(0, boardSize - 1)
            
        while not board[rowNum][colNum] == 0:
            rowNum = random.randint(0, boardSize - 1 )
            colNum = random.randint(0, boardSize - 1)
        board[rowNum][colNum] = pickNewValue()
        
        def won():
         for row in board:
            if 2048 in row:
                return True
            return False
            
        def noMoves():
            tempBoard1 = merge_down(tempBoard1)
            if tempBoard1 == tempBoard2:
                tempBoard1 = merge_up(tempBoard1)
                if tempBoard1 == tempBoard2:
                    tempBoard1 = merge_left(tempBoard1)
                if tempBoard1 == tempBoard2:  
                    tempBoard1 = merge_right(tempBoard1)
                if tempBoard1 == tempBoard2: 
                    return True
                return False
                    
        board = []
        for i in range(boardSize):
            row = []
            for j in range(boardSize):
                roe.append(0)
                board.append(row)
                
        numNeeded = 2
        while numNeeded > 0:
            rowNum = random.randint(0, boardSize - 1)
            colNum = random.randint(0, boardSize - 1)
            
        if board[rowNum][colNum] == 0:
            board[rowNum][colNum] = pickNewValue()
            numNeeded -= 1
            
        print("Welcome to 2048, you all already know the rules . you will have to press d to move right direction , w to move up , a to move left and s to move down.\n\n Here is the starting board:")
        display()
            
        gameOver = False
            
        while not gameOver:
                move = input("Which way do you want to merge? ")
                
                validInput = True
                tempBoard = copy.deepcopy(board)
                
                if move == "d":
                    board = merge_right(board)
                     
                elif move == "w":
                    board = merge_up(board)
                elif move == "a":
                    board = merge_left(board)
                elif move == "s":
                    board = merge_down(board)
                    
                else:
                    validInput = False
                    
                    
                    if not validInput:
                        print("Your input was not valif , please try again")
                        
                    else:
                            if board == tempBoard:
                                print("try a different direction")
                            else:
                                    if won():
                                        display()
                                        print("you won")
                                        gameOver = True
                                    else:
                                     addNewValue()
                            display()
                            
                            if noMoves():
                                print(" no more moves possible , you lose ")
                                gameOver = True
