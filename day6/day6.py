file_path = "document"
pattern = r"\d+"

import re

with open(file_path, 'r') as file:
    i = 0
    for line in file:
        if i == 0:
            times = re.findall(pattern, line)
        if i == 1:
            distance = re.findall(pattern, line)
        i += 1
print(times)
print(distance)
def race_sim(time, hold):
    drive_time = time - hold
    speed = hold
    print(drive_time * speed)
    return drive_time * speed


numbers = []

for x in range(len(times)):
    possible_races = 0
    for y in range(0, int(times[x]) + 1):
        if race_sim(int(times[x]), y) > int(distance[x]):
            possible_races += 1

    numbers.append(possible_races)

import numpy as np

result = np.prod(np.array(numbers))
print(result)