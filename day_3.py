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

# day 3 Q 2
# it's time to write some functions

def drop_items(binaries_list, digit, value_to_keep):
    # Function to remove items from list of binaries based on the value of digit using list comprehension
    #     
    binaries = [item for item in binaries_list if item[digit] == value_to_keep]

    return binaries



def most_common_bit(binaries_list, digit):
    count_0 = 0
    count_1 = 0
    for item in range(len(binaries_list)):
        if binaries_list[item][digit] == '1':
            count_1 += 1
        else:
            count_0 +=1
    
    if count_1 > count_0:
        CO2 = '1'
    elif count_1 == count_0:
        CO2 = '1'
    else:
        CO2 = '0'

    return CO2

def least_common_bit(binaries_list, digit): 
    count_0 = 0
    count_1 = 0
    for item in range(len(binaries_list)):
        if binaries_list[item][digit] == '1':
            count_1 += 1
        else:
            count_0 +=1
    
    if count_1 > count_0:
        O2 = '0'
    elif count_1 == count_0:
        O2 = '0'
    else: 
        O2 = '1'

    return O2

# for the CO2 rating

binaries_loaded = []
with open('day_3.txt', 'r') as input3:
    for line in input3:
        binaries_loaded.append(line)


CO2_rating = ''
O2_rating = '' 

binaries_temp_CO2 = binaries_loaded
binaries_temp_O2 = binaries_loaded

for position in range(12):

    if len(binaries_temp_CO2) > 1:
        CO2_append =  most_common_bit(binaries_temp_CO2, position)
        binaries_temp_CO2 = drop_items(binaries_temp_CO2, position, CO2_append)
        CO2_rating = CO2_rating + CO2_append
    else:
        CO2_rating = binaries_temp_CO2[0]

    if len(binaries_temp_O2) > 1:
        O2_append =  least_common_bit(binaries_temp_O2, position)
        binaries_temp_O2 = drop_items(binaries_temp_O2, position, O2_append)
        O2_rating = O2_rating + O2_append
    else:
        O2_rating = binaries_temp_O2[0]

print (CO2_rating)
print(O2_rating)

CO2_nonbin = int(CO2_rating, 2)  
O2_nonbin = int(O2_rating, 2)       

answer = CO2_nonbin*O2_nonbin

print(answer)