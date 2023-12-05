def parse_file(file: str):
    with open(file, 'r') as f:
        num_list = f.readlines()
    num_list = [num.strip() for num in num_list]
    return num_list

def first_and_last_combine(calibration: str):
    numbers: str = ""
    for c in calibration:
        if c.isnumeric():
            numbers += c
    return int(numbers[0] + numbers[-1])

    

cal_list = parse_file('input.txt')

num_list = []

for cal in cal_list:
    num_list.append(first_and_last_combine(cal))

print(sum(num_list))