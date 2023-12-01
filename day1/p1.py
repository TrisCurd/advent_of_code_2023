def interpretLine(line: str):
    numbers_in_line = []
    for char in line:
        if char.isnumeric():
            numbers_in_line.append(int(char))
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



