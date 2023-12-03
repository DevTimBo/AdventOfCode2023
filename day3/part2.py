import re


def find_full_number(arr, index):
    left_index = index
    right_index = index

    while left_index > 0 and arr[left_index - 1].isdigit():
        left_index -= 1

    while right_index < len(arr) - 1 and arr[right_index + 1].isdigit():
        right_index += 1

    full_number = ''.join(arr[left_index:right_index + 1])

    return full_number, left_index, right_index + 1


file_path = 'full'
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
        for y in range(len(array[x])):
            numbers = []
            if array[x][y] == '*':

                if y - 1 < 0 and y + 2 > len_line:
                    break

                if x > 0:
                    old_left = None
                    old_right = None
                    for z in range(y - 1, y + 2):

                        if str(array[x - 1][z]).isdigit():
                            number, left, right = find_full_number(array[x - 1], z)
                            if left != old_left and right != old_right:
                                if number:
                                    numbers.append(number)
                                    old_left = left
                                    old_right = right
                old_left = None
                old_right = None
                for z in range(y - 1, y + 2, 2):

                    if str(array[x][z]).isdigit():
                        number, left, right = find_full_number(array[x], z)
                        if left != old_left and right != old_right:
                            if number:
                                numbers.append(number)
                                old_left = left
                                old_right = right
                old_left = None
                old_right = None
                if x < len(array) - 1:

                    for z in range(y - 1, y + 2):
                        if str(array[x + 1][z]).isdigit():
                            number, left, right = find_full_number(array[x + 1], z)
                            if left != old_left and right != old_right:
                                if number:
                                    numbers.append(number)
                                    old_left = left
                                    old_right = right

            print(numbers)
            if len(numbers) == 2:
                sum += int(numbers[0]) * int(numbers[1])

    print(sum)
