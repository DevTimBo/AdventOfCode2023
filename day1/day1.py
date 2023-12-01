import re

file_path = 'day1/document'
pattern = r'\d'
set_strings = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

with open(file_path, 'r') as file:
    sum = 0
    for line in file:
        i = 1
        for string in set_strings:
            if line.find(string) != -1:
                line = line.replace(string, string + str(i) + string)
            i += 1

        numbers = re.findall(pattern, line.strip())
        number_string = f'{numbers[0]}{numbers[-1]}'
        number = int(number_string)
        sum += number

print(sum)
