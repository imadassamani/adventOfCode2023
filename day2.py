import re
import math

def isValidGame(game):
    rounds = game.split(";")
    for round in rounds:
        red_match = re.search(r'(\d+) red', round)
        blue_match = re.search(r'(\d+) blue', round)
        green_match = re.search(r'(\d+) green', round)
        if red_match and int(red_match.group(1)) > total_red:
            return False
        if blue_match and int(blue_match.group(1)) > total_blue:
            return False
        if green_match and int(green_match.group(1)) > total_green:
            return False
    return True

def getHighestColor(game):
    red, blue, green = 0, 0, 0
    rounds = game.split(";")
    for round in rounds:
        red_match = re.search(r'(\d+) red', round)
        blue_match = re.search(r'(\d+) blue', round)
        green_match = re.search(r'(\d+) green', round)
        if red_match and int(red_match.group(1)) > red:
            red = int(red_match.group(1))
        if blue_match and int(blue_match.group(1)) > blue:
            blue = int(blue_match.group(1))
        if green_match and int(green_match.group(1)) > green:
            green = int(green_match.group(1))
    return red, blue, green

def part1(file):
    part1_results = []
    for line in file:
        line_array = line.split(":")
        game_id = line_array[0]
        game_data = line_array[1]
        game_id = re.search(r'Game (\d+)', game_id)
        result = isValidGame(game_data)
        if (result):
            part1_results.append(int(game_id.group(1)))
    return part1_results

def part2(file):
    part2_results = []
    for line in file:
        line_array = line.split(":")
        game_data = line_array[1]
        result = getHighestColor(game_data)
        part2_results.append(math.prod(result))
    return part2_results

# Open file, define total cubes for part 1
file = open("./data/day2.txt", "r")
total_red = 12
total_green = 13
total_blue = 14

######### PART 1 ##############
print(sum(part1(file)))
# Rewind cursor to beginning
file.seek(0)
######### PART 2 ##############
print(sum(part2(file)))

# Never forget closing files. We don't want too much file descriptors open
file.close()