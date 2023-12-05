# Parse input file
with open('input.txt', 'r') as f:
    schematic = f.readlines()
schematic = [num.strip() for num in schematic]

# Could add a check for not stepping out of range, but isn't necessary for this task
def find_adjacent_num_elems(coords):
    i, j = coords
    arr = []
    # Above
    arr.append(schematic[i-1][j-1])
    arr.append(schematic[i-1][j])
    arr.append(schematic[i-1][j+1])

    # Sides
    arr.append(schematic[i][j-1])
    arr.append(schematic[i][j+1])

    #Bellow
    arr.append(schematic[i+1][j-1])
    arr.append(schematic[i+1][j])
    arr.append(schematic[i+1][j+1])

    return arr

numeric_coords = []

def find_numeric_coords(coords):
    i, j = coords
    # Above
    if schematic[i-1][j-1].isnumeric():
        numeric_coords.append((i-1, j-1))

    if schematic[i-1][j].isnumeric():
        numeric_coords.append((i-1, j))
        
    if schematic[i-1][j+1].isnumeric():
        numeric_coords.append((i-1, j+1))

    # Sides
    if schematic[i][j-1].isnumeric():
        numeric_coords.append((i, j-1))
    
    if schematic[i][j-1].isnumeric():
        numeric_coords.append((i, j+1))

    #Bellow
    if schematic[i+1][j-1].isnumeric():
        numeric_coords.append((i+1, j-1))

    if schematic[i+1][j].isnumeric():
        numeric_coords.append((i+1, j))
        
    if schematic[i+1][j+1].isnumeric():
        numeric_coords.append((i+1, j+1))

    return numeric_coords

def get_entire_number(coords):
    i, j = coords

    entire_number = schematic[i][j]

    left_j: int = j-1
    left_char = schematic[i][left_j]
    # Check left
    while left_char.isnumeric():
        entire_number = left_char + entire_number
        left_j -= 1
        left_char = schematic[i][left_j]
        
    # Check right
    right_j: int = j+1
    right_char = schematic[i][right_j]
    while right_char.isnumeric():
        entire_number = entire_number + right_char
        if right_j < 139:
            right_j += 1
        else:
            break
        right_char = schematic[i][right_j]

    return entire_number


# Firstly, get all coords of the special symbols

special_symbols_loc = []
for i in range(len(schematic)):
    for j in range(len(schematic[0])):
        if not schematic[i][j].isnumeric() and schematic[i][j] != '.':
            special_symbols_loc.append((i, j))


for symbol in special_symbols_loc:
    find_numeric_coords(symbol)

# Has to have unique coords 
# Taken from w3schools 
# (apparently makes no difference lol)
numeric_coords = list(dict.fromkeys(numeric_coords))

# print(numeric_coords[0])

sum = 0

previous_num = ""

for coord in numeric_coords:
    number = get_entire_number(coord)
    if '.' in number:
        continue
    if number != previous_num:
        print(f"{coord} got {number}")
        sum += int(number)
    previous_num = number
print(sum)