sum = 0

# Parse input file
with open('input.txt', 'r') as f:
    input_list = f.readlines()
input_list = [num.strip() for num in input_list]

# Iterate over all rows in previously read file
for row in input_list:
    divided = row.replace('Game ', '').split(': ')
    id = int(divided[0])
    rest = divided[1]

    rest_listed = rest.split('; ')

    max_green = 0
    max_blue = 0
    max_red = 0
    # For a certain id we will have to get the highest amount of each color
    for color_strings in rest_listed:
        color_count_list = color_strings.split(', ')
        print(color_count_list)
        for color_count in color_count_list:
            cn = color_count.split(' ')
            color = cn[1]
            count = int(cn[0])
            if color == 'green':
                if count > max_green:
                    max_green = count

            if color == 'blue':
                if count > max_blue:
                    max_blue = count

            if color == 'red':
                if count > max_red:
                    max_red = count
    
    sum += max_blue * max_green * max_red
#     if max_green <= 13 and max_blue <= 14 and max_red <= 12:
#         sum += id

print(sum)