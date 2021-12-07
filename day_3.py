# Load input day 3

binaries = []
with open('day_3.txt', 'r') as input3:
    for line in input3:
        binaries.append(line)

print(type(binaries[0][11]))

gamma = ''
epsilon = ''
for index in range(len(binaries[0])-1):
    count_0 = 0
    count_1 = 0
    for item in range(len(binaries)):
        if binaries[item][index] == '1':
            count_1 +=1
        else:
            count_0 +=1

    if count_1 > count_0:
        gamma = gamma + '1'
        epsilon = epsilon + '0'
    else:
        gamma = gamma + '0'
        epsilon = epsilon + '1'

print('gamma = ' + gamma)
print('epsilon = '+ epsilon )

gamma_nonbin = int(gamma, 2)  
epsilon_nonbin = int(epsilon, 2)     

result = gamma_nonbin * epsilon_nonbin
print(result)



       