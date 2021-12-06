
#load the input data of day 1
input1 = open('day_1.txt').read().splitlines()

input1 = list(map(int, input1))
count = 0

# Count the number of increases in dept measurement
for i in range(len(input1)):
    if i != 0:
        if input1[i-1] < input1[i]:
            count +=1

# print the result 
print(count)