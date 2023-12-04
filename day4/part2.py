import re

file_path = 'document'
pattern = r'\d+'


def find_value(arr, target):
    try:
        index = arr.index(target)
        return index
    except ValueError:
        return -1


full_card_array = []
full_first_array = []
full_second_array = []

with open(file_path, 'r') as file:
    total = 0

    for line in file:
        card_line = line.split(":")[0]
        line = line.split(":")[1]
        firstLine = line.split("|")[0]
        secondLine = line.split("|")[1]
        firstArray = re.findall(pattern, firstLine)
        secondArray = re.findall(pattern, secondLine)
        card_array = re.findall(pattern, card_line)
        full_card_array.append(card_array)
        full_first_array.append(firstArray)
        full_second_array.append(secondArray)

scratchcards = 0
x = 0
original_len = len(full_second_array)

while x < len(full_second_array):
    print(scratchcards)
    y = int(full_card_array[x][0]) - 1

    scratchcards += 1
    times = 0
    for i in range(len(full_second_array[x])):

        if find_value(full_first_array[x], full_second_array[x][i]) != -1:
            times += 1

    for u in range(y, y + times):
        if u + 1 >= original_len:
            break
        else:
            full_card_array.append(full_card_array[u + 1])
            full_first_array.append(full_first_array[u + 1])
            full_second_array.append(full_second_array[u + 1])

    x += 1
print(scratchcards)

