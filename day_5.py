
import numpy as np

# load the inputs
coordinates = []
with open('day_5.txt', 'r') as input5:
    for line in input5:
        a, b = line.split('->')
        a1, a2 = a.split(',')
        b1, b2 = b.split(',')
        b1, b2 = map(int, [b1, b2])
        a1, a2 = map(int, [a1, a2])
        coordinates.append([[a1, a2], [b1, b2]])

# Create a grid of 1000x1000 filled with .
grid = np.zeros(shape = (1000, 1000))

# function to check a pair of coordinates
# first check if its horizontal or vertical
# then generate list of coordinates that are affected
# then change the entry in the grid for each coordinate in the list from a pair

def hor_or_ver(pair):
    if pair[0][0] == pair[1][0]:
        direction = 'Vertical'
    else:
        direction = 'Horizontal'
    return direction

def find_all_points(pair, direction):
    # add some lines for if the line is in opposite direction
    list_of_coordinates = []
    if direction == 'Horizontal':
        list_of_coordinates.append(pair[0])
        step_size = abs(pair[0][0] - pair[1][0])
        for i in range(step_size):
            list_of_coordinates.append([pair[0][0] + (i+1), pair[0][1]])
    else:
        list_of_coordinates.append(pair[0])
        step_size = abs(pair[0][1] - pair[1][1])
        print(step_size)
        for j in range(step_size):
            list_of_coordinates.append([pair[0][0], pair[0][1] + (j+1)])
    return list_of_coordinates

def adjust_grid(grid, list_of_coordinates):
    for coordinate in list_of_coordinates:
        grid[coordinate[1]][coordinate[0]] += 1
    return grid

for pair in coordinates:
    print(pair)
    direction = hor_or_ver(pair)
    print(direction)
    list_of_coordinates = find_all_points(pair, direction)
    print(list_of_coordinates)
    grid = adjust_grid(grid, list_of_coordinates)