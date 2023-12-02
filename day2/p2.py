#need to read each line and get the id, the # for each color that was pulled

def readInput():
    #read input
    file = open("./input.txt", "r")
    lines = file.readlines()
    interpretedList = []
    for line in lines:
        interpretation = interpretLine(line)
        interpretedList.append(interpretation)
    return interpretedList
        

def interpretLine(line: str):    
    gameString, resultsString = line.split(":")
    numGame = int(gameString.split(" ")[-1])
    resultsString = resultsString.replace(";",",")
    counts = resultsString.split(",")

    redVals = [0]
    greenVals = [0]
    blueVals = [0]

    for count in counts:
        #print(f"count = {count} split up = {count.split(' ')}")
        #excess doesn't matter, it's extra whitespace
        count = count.strip()
        num, color = count.split(" ")
        num = int(num)
        match color:
            case "red":
                redVals.append(num)
            case "green":
                greenVals.append(num)
            case "blue":
                blueVals.append(num)
            case _:
                print(f"something went wrong with {color}.\n the count was {count} and the split was {count.split(' ')}")

    numRed = max(redVals)
    numGreen = max(greenVals)
    numBlue = max(blueVals)

    return [numGame, numRed, numGreen, numBlue]
      
def calculatePower(inputs: list): 
    powerList = []
    for input in inputs:
        power = input[1] * input[2] * input[3]
        powerList.append(power)
    return powerList


goodList = readInput()
finalList = calculatePower(goodList)
print(sum(finalList))