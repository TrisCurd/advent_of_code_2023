from script import readInput
import re

def checkValidity(inputs: list):
    validNumbers = []
    for row in range(len(inputs)):
        for col in range(len(lines[row])):
            #check each symbol, see if there's a number in the area around it
            currSymbol = lines[row][col]
            if re.match("[^0-9\.\n]",currSymbol):
                numbersAround = checkArea(inputs,row,col)
                for number in numbersAround:
                    validNumbers.append(number)
    return validNumbers

def checkArea(map: list[str], row: int, col: int):
    validNumbers = []
    if row > 0:
        topRow = map[row-1]
        if col > 0:
            leftInd = col-1
            leftPos = topRow[leftInd]
            mid = topRow[col]
            rightInd = col+1
            rightPos = topRow[rightInd]
            if mid.isnumeric():
                #check left and right
                numString = mid
                while topRow[leftInd].isnumeric() and leftInd >=0:
                    left = topRow[leftInd]
                    numString = left + numString
                    leftInd -= 1
                while topRow[rightInd].isnumeric() and rightInd < len(topRow):
                    right = topRow[rightInd]
                    numString = numString
                    rightInd += 1
                num = int(numString)
                validNumbers.append
                
            else:
                if left.isnumeric():
                #check just left
                if right.isnumeric():
                #check right

    if row < len(map) - 1:
        botRow = map[row+1]
    midRow = map[row]

    return validNumbers





lines = readInput("./input.txt")
validNumbers = checkValidity(lines)
#looks like all numbers only are next to 1 symbol