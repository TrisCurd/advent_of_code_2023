numPad = {
    'one': 1,
    'two':2,
    'three':3,
    'four':4,
    'five':5,
    'six':6,
    'seven':7,
    'eight':8,
    'nine': 9,
}

def interpretLine(line: str):
    numbers_in_line = []
    for i in range(len(line)):
        char = line[i]
        if char.isnumeric():
            numbers_in_line.append(int(char))
        else:
            #need to check if there are digits spelled out now
            #all are either 3-5 letters long
            if (i + 3) < len(line):
               three_letter = line[i:i+3]
               if three_letter in numPad:
                    print(f"3: {three_letter}")
                    numbers_in_line.append(numPad[three_letter])
            if (i + 4) < len(line):
                four_letter = line[i:i+4]
                if four_letter in numPad:
                    print(f"4: {four_letter}")
                    numbers_in_line.append(numPad[four_letter])
            if (i + 5) < len(line):
                five_letter = line[i:i+5]
                if five_letter in numPad:
                    print(f"5: {five_letter}")
                    numbers_in_line.append(numPad[five_letter])     
    #add 1st and last digit
    returnNum = (numbers_in_line[0] * 10) + numbers_in_line[-1]
    return returnNum 



#read input
file = open("./input.txt", "r")
lines = file.readlines()
numbers = []


for line in lines:
    curr_num = interpretLine(line)
    numbers.append(curr_num)

total = sum(numbers)

print(total)



