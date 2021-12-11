import numpy as np

def draw_numbers(numbers, drawn_numbers):
    # Function to draw the next 5 numbers
    for i in range(5):
        drawn_numbers.append(numbers[0])
        numbers.pop(0)
    return drawn_numbers

def check_bingocard(card, drawn_numbers):
    #function that chacks if a card has bingo 
    for list in card:
        comparison = set(list) & set(drawn_numbers)
        if len(comparison) == 5:
            Bingo = True
            return Bingo

    card_to_array = np.array(card)
    transpose = card_to_array.T
    card_transpose = transpose.tolist()

    for list_t in card_transpose:
        comparison_transpose = set(list_t) & set(drawn_numbers)
        if len(comparison_transpose) == 5:
            Bingo = True
            return Bingo

    Bingo = False
    return Bingo

def find_answer(card, drawn_numbers):
    numbers=[]
    for list in card:
           

# Lets load the bingocards
full_input = []
with open('day_4.txt', 'r') as input4:
    for line in input4:
        full_input.append(line)


print(full_input[0][-1])

# Read the drawn numbers from the input file
numbers = full_input[0].split(',')
map_object = map(int, numbers)
numbers = list(map_object)
full_input.pop(0)


# Read the different bingocards to grids and put in list
# each item in the bingocards list is 1 bingocard grid

bingo_cards_input = full_input
bingo_cards_input.pop(0)
card_nr = -1
bingocards = []
grid = []

for line in bingo_cards_input:
    if line == '\n':
        bingocards.append(grid)
        grid = []
        card_nr +=1
    else:
        row = line.split()
        map_row = map(int, row)
        row_final = list(map_row)
        grid.append(row_final)
        

drawn_numbers = []
for i in range(len(drawn_numbers)/5):
    drawn_numbers = draw_numbers(numbers, drawn_numbers)
    for card in bingo_cards_input:
        bingo = check_bingocard(card, drawn_numbers)
        if bingo == True:
            # doe hier de functie die het antwoord geeft
            answer = []
            print(answer)
            


        

