# solving the questions of day 2 of the adevent of code
# Load the input of day 2
input2 = open('day_2.txt').read().splitlines()

dictionary = dict()
with open('day_2.txt', 'r') as input2:
    for line in input2:
        command,value = line.split()

        if command in dictionary:
            dictionary[command].append(int(value))
        else:
            dictionary[command] = [int(value)]

forward = sum(dictionary['forward'])
down = sum(dictionary['down'])
up = sum(dictionary['up'])

dept = down - up

answer = forward*dept
print(answer)