import math


arr_down = [1,1,1,1,2]      # number of tiles we move each time
arr_sideways = [1,3,5,7,1]  # if we go left it's negative integer, else it's positive



continue_row_n_times = lambda row, n: [row[i%len(row)] for i in range(n*len(row))]



with open("./input_data.txt", "r") as input_file:
    input_data = input_file.read()

forest_part = [list(i) for i in input_data.split("\n")]

all_slopes = []

for down, sideways in zip(arr_down, arr_sideways):
    pos_x = 0
    pos_y = 0

    n_forest_repetas = (len(forest_part)/down) / (len(forest_part[-1]) / sideways) # number of moves downward / number of sideways moves in one forest part = number of forest parts we need to go all the way down 
    n_forest_repetas = math.ceil(n_forest_repetas) + 1 # we add one to be sure that we have enough forest parts to go all the way down


    forest = [continue_row_n_times(i, n_forest_repetas) for i in forest_part]


    trees_encountered = 0

    while True:
        try:
            if forest[pos_y][pos_x] == "#":
                trees_encountered += 1
        
        except IndexError:
            break

        pos_x += sideways
        pos_y += down

    all_slopes.append(trees_encountered)

result = 1
for i in all_slopes:
    result *= i

print(result)