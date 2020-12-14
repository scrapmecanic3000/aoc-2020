import numpy as np 
  
def unique(arr): 
    x = np.array(arr) 
    return np.unique(x)

def prepare_data(data):
    data = data.split("\n\n")
    data = [i.split("\n") for i in data]
    
    return data

def group_answers(group):
    result = []
    
    for i in group:
        result += i
    
    return list(unique(result))

with open("C:/Users/Lenovo T440/Desktop/aoc-2020/day_6/input_data.txt", "r") as input_file:
    input_data = input_file.read()

answers = prepare_data(input_data)

unique_answers = [group_answers(i) for i in answers]

n_of_unique_answers = [len(i) for i in unique_answers]

print(sum(n_of_unique_answers))






