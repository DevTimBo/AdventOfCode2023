import re
import time

seed_list = []
seed_to_soil_map = dict()
soil_to_fertilizer_map = dict()
fertilizer_to_water_map = dict()
water_to_light_map = dict()
light_to_temperature_map = dict()
temperature_to_humidity_map = dict()
humidity_to_location = dict()

file_path = 'document'
pattern = r'\d+'

def mapping_fun(map_number):

    numbers = re.findall(pattern, line)
    dest_start = int(numbers[0])
    source_start = int(numbers[1])
    range_len = int(numbers[2])
    dest_end = dest_start + range_len
    source_end = source_start + range_len
    maps = {
        1: seed_to_soil_map,
        2: soil_to_fertilizer_map,
        3: fertilizer_to_water_map,
        4: water_to_light_map,
        5: light_to_temperature_map,
        6: temperature_to_humidity_map,
        7: humidity_to_location
    }

    current_map = maps.get(map_number)

    if current_map is not None:
        current_map[(source_start, source_end)] = (dest_start, dest_end)

    else:
        print(f"Error: Map {map_number} not found.")



with open(file_path, 'r') as file:
    map_number = 0
    for line in file:
        start = time.time()
        line = line.strip()
        if len(line) == 0:
            map_number = 0
            continue
        if map_number == 0:
            # Fill Seed List
            line_split = line.split(":")[0]
            if line_split == "seeds":
                seed_list = re.findall(pattern, line)
                seed_list = [int(number) for number in seed_list]
            # Activate Map Number
            elif line_split == "seed-to-soil map":
                map_number = 1
                continue
            elif line_split == "soil-to-fertilizer map":
                map_number = 2
                continue
            elif line_split == "fertilizer-to-water map":
                map_number = 3
                continue
            elif line_split == "water-to-light map":
                map_number = 4
                continue
            elif line_split == "light-to-temperature map":
                map_number = 5
                continue
            elif line_split == "temperature-to-humidity map":
                map_number = 6
                continue
            elif line_split == "humidity-to-location map":
                map_number = 7
                continue
        else:

            mapping_fun(map_number)

        print(time.time() - start)

def is_value_in_range(value, my_dict):
    for key in my_dict:
        if key[0] <= value <= key[1]:
            return key
    return -1, value
def find_number_in_dict(dict, number):
    source_start, source_end = is_value_in_range(number,dict)
    if source_start != -1:
        dest_start, dest_end = dict[(source_start, source_end)]
        pad = number - source_start
        next_key = dest_start + pad
    else:
        next_key = number
    return next_key

seed_locations = []



for seed in seed_list:
    soil = find_number_in_dict(seed_to_soil_map, seed)
    fertilizer = find_number_in_dict(soil_to_fertilizer_map, soil)
    water = find_number_in_dict(fertilizer_to_water_map, fertilizer)
    light = find_number_in_dict(water_to_light_map, water)
    temp = find_number_in_dict(light_to_temperature_map, light)
    humidity = find_number_in_dict(temperature_to_humidity_map, temp)
    location = find_number_in_dict(humidity_to_location, humidity)
    seed_locations.append(location)

print(min(seed_locations))