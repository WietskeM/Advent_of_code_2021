
#load the input data of day 1
input1 = open('day_1.txt').read().splitlines()

input1 = list(map(int, input1))
count = 0

# Count the number of increases in dept measurement (Q1)
for i in range(len(input1)):
    if i != 0:
        if input1[i-1] < input1[i]:
            count +=1

# print the result 
print(count)

#now for the sums (Q2)
sum_list = []

# create list with the shifting windows sums
for i in range(len(input1)):
    if i < len(input1)-2:
        sum_list.append(input1[i]+input1[i+1]+input1[i+2])

#count the number of increases
count2 = 0
for i in range(len(sum_list)):
    if i != 0:
        if sum_list[i-1]<sum_list[i]:
            count2 +=1

print(count2)
