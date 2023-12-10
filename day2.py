import re

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

file = open("./data-day2.txt", "r")
total_red = 12
total_green = 13
total_blue = 14

results = []
for line in file:
    line_array = line.split(":")
    game_id = line_array[0]
    game_data = line_array[1]
    game_id = re.search(r'Game (\d+)', game_id)
    result = isValidGame(game_data)
    if (result):
        results.append(int(game_id.group(1)))
print(sum(results))


file.close()