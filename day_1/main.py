def sum_of_pair(_input, _sum):
    for i in _input:
        for j in _input:
            if i + j == _sum:
                return i, j
            if i == j:
                continue

with open("./input_data.txt", "r") as input_file:
    input_data = input_file.read()

_input = [int(i) for i in input_data.split("\n")]
i, j = sum_of_pair(_input, 2020)
print(i*j)