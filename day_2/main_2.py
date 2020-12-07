def trasnform_into_dict(arr):
    from_i, to_i = arr[0].split("-")
    final_dict = {"pos_1": int(from_i), "pos_2": int(to_i), "letter": arr[1][0], "password": arr[2]}
    
    return final_dict


with open("./input_data.txt", "r") as input_file:
    input_data = input_file.read()

_input_raw = [i.split(" ") for i in input_data.split("\n")]
_input = []

for i in _input_raw:
    _input.append(trasnform_into_dict(i))

total_right_passwords = sum([1 for i in _input if (i["password"][i["pos_1"]-1] == i["letter"]) ^ (i["password"][i["pos_2"]-1] == i["letter"])])

print(total_right_passwords)