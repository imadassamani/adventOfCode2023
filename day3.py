
symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_","+", "="]
file = open("./data/day3.txt", "r")
data = file.read()
array_data = data.split("\n")
final_result = 0
for y in range(140):
    for x in range(140):
        try:
            num = int(array_data[y][x])
            collect_surrounding = []
            if (y > 0 and x > 0 and y+1 < 140 and x+1 < 140):
                collect_surrounding= [array_data[y-1][x-1], array_data[y-1][x], array_data[y-1][x+1],
                                            array_data[y][x-1], array_data[y][x+1],
                                            array_data[y+1][x-1],array_data[y+1][x],array_data[y+1][x+1]]
            elif (y == 0 and x == 0):
                collect_surrounding = [ array_data[y][x+1], array_data[y+1][x+1]]
            elif (y+1 == 140 and x+1 == 140):
                collect_surrounding = [array_data[y-1][x-1], array_data[y-1][x], array_data[y][x-1]]
            elif (y == 0 and x+1 == 140):
                collect_surrounding = [array_data[y][x-1], array_data[y+1][x-1]]
            elif (x == 0 and y+1 == 140):
                collect_surrounding = [ array_data[y-1][x], array_data[y-1][x+1],array_data[y][x+1]]
            elif (x == 0):
                collect_surrounding = [ array_data[y-1][x], array_data[y-1][x+1],array_data[y][x+1] ,array_data[y+1][x+1]]
            elif (y == 0):
                    collect_surrounding = [array_data[y][x-1],array_data[y][x+1], 
                                   array_data[y+1][x-1],array_data[y+1][x+1]]
            elif (y+1 == 140):
                collect_surrounding = [array_data[y-1][x-1], array_data[y-1][x], array_data[y-1][x+1], 
                                   array_data[y][x-1],array_data[y][x+1]]
            elif (x+1 == 140):
                collect_surrounding = [array_data[y-1][x-1], array_data[y-1][x], array_data[y][x-1], array_data[y+1][x-1]]
            has_symbol = filter(lambda x: x in symbols, collect_surrounding)
            symbol_list = list(has_symbol)
            if (len(symbol_list) > 0):
                final_result+=num
        except ValueError:
            pass 
print(final_result)       
file.close()