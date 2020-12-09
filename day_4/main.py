import re

def convert_to_dict(a):
    try:
        result_dict = dict([(i.split(":")[0], i.split(":")[1]) for i in a])
        return result_dict
    except:
        print(a)

def is_valid(passport):
    is_valid = False
    try:
        return 1920 <= int(passport["byr"]) <= 2002 \
            and 2010 <= int(passport["iyr"]) <= 2020 \
            and 2020 <= int(passport["eyr"]) <= 2030 \
            and passport["hcl"][0] == "#" and len(passport["hcl"][1:]) == 6 \
            and ((passport["hgt"][-2:] == "cm" and int(passport["hgt"][:-2]) in range(150, 193+1)) \
            or  (passport["hgt"][-2:] == "in" and int(passport["hgt"][:-2]) in range(59, 76+1))) \
            and passport["ecl"] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"] \
            and len(passport["pid"])==9 
    except KeyError:
        return False


with open("./input_data.txt", "r") as input_file:
    input_data = input_file.read()

credentials_raw = input_data.split("\n\n")  # split our dat into passports
credentials = [re.split("[\s, \n]", i) for i in credentials_raw]

passports = [convert_to_dict(i) for i in credentials]

passport_validity = [is_valid(i) for i in passports]

print(sum(passport_validity))
