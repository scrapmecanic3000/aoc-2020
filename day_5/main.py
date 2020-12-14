
def prepare_data(data):
    result_data = []
    
    divided_data = data.split("\n")
    result_data = [[i[:-3], i[-3:]] for i in divided_data]

    result_data = [[i[0].replace("F", "L"), i[1].replace("R", "M")] for i in result_data]
    result_data = [[i[0].replace("B", "M"), i[1].replace("L", "L")] for i in result_data]


    return result_data

def find_place_in_range(bounds, commands, ind=0):
    
    half_of_bounds_range = ( ( (bounds[1] - bounds[0]) +1) /2)

    if ind <= (len(commands) - 1):
        if commands[ind] == "M":
            ind += 1
            return find_place_in_range([bounds[0] + half_of_bounds_range, bounds[1]], commands, ind)
        else:
            ind += 1
            return find_place_in_range([bounds[0], bounds[1] - half_of_bounds_range], commands, ind) 
    else:
        return round(bounds[0])



with open("C:/Users/Lenovo T440/Desktop/aoc-2020/day_5/input_data.txt", "r") as input_file:
    input_data = input_file.read()



boarind_passes = prepare_data(input_data)

rows = [find_place_in_range([0, 127], i[0]) for i in boarind_passes]
columns = [find_place_in_range([0, 7], i[1]) for i in boarind_passes]
rw_n_cl = list(zip(rows, columns))

ids = [i[0] * 8 + i[1] for i in rw_n_cl]
print(max(ids))

