import re

def convert_to_dict(a):
    try:
        result_dict = dict([(i.split(":")[0], i.split(":")[1]) for i in a])
        return result_dict
    except:
        print(a)

def is_valid(passport):
    is_valid = False

    if len(passport.keys()) == 8:   
        if 1920 <=  int(passport["byr"]) <= 2002 and 2010 <= int(passport["iyr"]) <= 2020 and 2020 <= int(passport["eyr"]) <= 2030 and ((bool(re.search("cm", passport["hgt"])) and int(re.split("cm", passport["hgt"])[0]) in range(150,193)) or (bool(re.search("[in]",passport["hgt"])) and int(re.split("in", passport["hgt"])[0]) in range(59, 76))) and bool(re.search("#([a-f]|[0-9]){6}", passport["hcl"])) and passport["ecl"] in ["amb","blu","brn","gry","grn","hzl","oth"] and bool(re.search("^([0-9]{9})$", passport["pid"])):
            return True
        else:
            return False
    elif len(passport.keys()) == 7:
        try:
            if 1920 <=  int(passport["byr"]) <= 2002 and 2010 <= int(passport["iyr"]) <= 2020 and 2020 <= int(passport["eyr"]) <= 2030 and ((bool(re.search("cm", passport["hgt"])) and int(re.split("cm", passport["hgt"])[0]) in range(150,193)) or (bool(re.search("[in]",passport["hgt"])) and int(re.split("in", passport["hgt"])[0]) in range(59, 76))) and bool(re.search("#([a-f]|[0-9]){6}", passport["hcl"])) and passport["ecl"] in ["amb","blu","brn","gry","grn","hzl","oth"] and bool(re.search("^([0-9]{9})$", passport["pid"])):
                return True
            else:
                return False
        except KeyError:
            return False
    else:
        return False
    
    return False



with open("c:/Users/Lenovo T440/Desktop/aoc-2020/day_4/input_data.txt", "r") as input_file:
    input_data = input_file.read()

credentials_raw = input_data.split("\n\n")  # split our dat into passports
credentials = [re.split("[\s, \n]", i) for i in credentials_raw]

passports = [convert_to_dict(i) for i in credentials]

passport_validity = [is_valid(i) for i in passports]

print(sum(passport_validity))