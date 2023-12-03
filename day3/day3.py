import re

file_path = 'document'
pattern = r'[^a-zA-Z0-9.]'

with open(file_path, 'r') as file:
    array = []
    i = 0
    for line in file:
        if i == 0:
            len_line = len(line.strip())
        array_line = []
        for j in range(len_line):
            array_line.append(line[j])

        array.append(array_line)
    sum = 0

    for x in range(len(array)):
        last_index = None
        for y in range(len(array[x])):
            if last_index != None and last_index >= y:
                continue
            if str(array[x][y]).isdigit():
                number = f'{array[x][y]}'
                start_index = y
                last_index = y
                for z in range(y + 1, len_line):
                    if str(array[x][z]).isdigit():
                        number = number + f"{array[x][z]}"
                        last_index = z
                    else:
                        break
                if start_index - 1 > 0:
                    if len(re.findall(pattern, str(array[x][start_index - 1]))) > 0:

                        sum = sum + int(number)
                        continue
                if last_index + 1 < len_line:
                    if len(re.findall(pattern, str(array[x][last_index + 1]))) > 0:

                        sum = sum + int(number)
                        continue
                for u in range(start_index - 1, last_index + 2):
                    if u < 0:
                        continue
                    if u > len_line-1:
                        continue
                    if x - 1 < 0:
                        break
                    if len(re.findall(pattern, str(array[x-1][u]))) > 0:
                        sum = sum + int(number)
                        continue
                for u in range(start_index - 1, last_index + 2):
                    if u < 0:
                        continue
                    if u > len_line-1:
                        continue
                    if x + 1 >= len(array) - 1:
                        break

                    if len(re.findall(pattern, str(array[x+1][u]))) > 0:

                        sum = sum + int(number)
                        continue

    print(sum)
        # if len(re.findall(pattern, line.strip())) > 0:
