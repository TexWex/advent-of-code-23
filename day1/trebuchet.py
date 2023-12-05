from collections import deque 

def parse_file(file: str):
    with open(file, 'r') as f:
        num_list = f.readlines()
    num_list = [num.strip() for num in num_list]
    return num_list

def word_to_num(str):
    word = str[:3]
    if word == 'one':
        return '1'
    if word == 'two':
        return '2'
    if word == 'six':
        return '6'
    
    word = str[:4]
    if word == 'four':
        return '4'
    if word == 'five':
        return '5'
    if word == 'nine':
        return '9'
    
    word = str[:5]
    if word == 'three':
        return '3'
    if word == 'seven':
        return '7'
    if word == 'eight':
        return '8'
    else:
        return ''

calibration_list = parse_file('input.txt')

acc_list = []

for cal in calibration_list:
    num_list = ""
    for i in range(len(cal)):
        if cal[i].isnumeric():
            num_list += cal[i]
        word = word_to_num(cal[i:i+5])
        if word.isnumeric():
            num_list += word

    acc_list.append(int(num_list[0] + num_list[-1]))

print(sum(acc_list))