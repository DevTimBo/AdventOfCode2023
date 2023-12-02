import re

file_path = 'document'
pattern = r'\d+'
red_cubes = 12
green_cubes = 13
blue_cubes = 14
separators = r'[;,:]'
single_pattern = r'(\d+) (\w+)'
with open(file_path, 'r') as file:
    game_id_sums = 0
    power_of_cubes = 0
    for line in file:

        game_id = -1
        red_n = list()
        green_n = list()
        blue_n = list()
        results = re.split(separators, line.strip())
        for res in results:
            if res.find("Game") != -1:
                game_id = int(re.findall(pattern, res)[0])
            elif res.find("blue") != -1:
                blue_n.append(int(re.findall(pattern, res)[0]))
            elif res.find("red") != -1:
                red_n.append(int(re.findall(pattern, res)[0]))
            elif res.find("green") != -1:
                green_n.append(int(re.findall(pattern, res)[0]))
        # Part 1
        #print(game_id, red_n, green_n, blue_n)
        # if max(red_n) <= red_cubes and max(green_n) <= green_cubes and max(blue_n) <= blue_cubes:
        #     game_id_sums += game_id
        power_of_cubes += max(red_n)*max(green_n)*max(blue_n)

print(power_of_cubes)