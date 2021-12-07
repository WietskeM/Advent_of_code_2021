# solving the questions of day 2 of the adevent of code
# Load the input of day 2

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

# question 2
command_list = []

with open('day_2.txt', 'r') as input2:
    for line in input2:
        command,value = line.split()
        command_list.append([command, int(value)])

hor = 0
aim = 0
dept2 = 0
for entry in command_list:
    if entry[0] == 'forward':
        hor = hor + entry[1]
        dept2 = dept2 + aim*entry[1]
    elif entry[0] == 'up':
        aim = aim - entry[1]
    elif entry[0] == 'down':
        aim = aim + entry[1]

answer2 = hor*dept2
print(answer2)
