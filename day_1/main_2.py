def sum_of_triple(_input, _sum):
    for i in _input:
        for j in _input:
            for k in _input:
                if i == j or j == k:
                    continue
                elif i + j + k== _sum:
                    return i, j, k

with open("./input_data.txt", "r") as input_file:
    input_data = input_file.read()

_input = [int(i) for i in input_data.split("\n")]
i, j, k = sum_of_triple(_input, 2020)
print(i*j*k)