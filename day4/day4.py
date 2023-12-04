import re

file_path = 'document'
pattern = r'\d+'


def find_value(arr, target):
    try:
        index = arr.index(target)
        return index
    except ValueError:
        return -1


with open(file_path, 'r') as file:

    for line in file:
        line = line.split(":")[1]
        firstLine = line.split("|")[0]
        secondLine = line.split("|")[1]
        firstArray = re.findall(pattern, firstLine)
        secondArray = re.findall(pattern, secondLine)


        points = 0
        for i in range(len(secondArray)):
            if find_value(firstArray, secondArray[i]) != -1:
                if points == 0:
                    points = 1
                else:
                    points = 2 * points
                    print("double")
        print(points)
        total += points


print(total)
