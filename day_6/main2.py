import numpy as np 
  
def everyone(arr): 
    unique_answers = [set(i) for i in arr]
    first_person = arr.pop(0)
    return list(set(first_person).intersection(*unique_answers))

def prepare_data(data):
    data = data.split("\n\n")
    data = [i.split("\n") for i in data]
    
    return data

with open("C:/Users/Lenovo T440/Desktop/aoc-2020/day_6/input_data.txt", "r") as input_file:
    input_data = input_file.read()

answers = prepare_data(input_data)

common_answers = [everyone(i) for i in answers]

n_of_unique_answers = [len(i) for i in common_answers]

print(sum(n_of_unique_answers))






