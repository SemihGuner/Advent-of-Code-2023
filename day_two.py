# https://pypi.org/project/advent-of-code-data/
import aocd
import numpy
import re
entry = aocd.get_data(day=2,year=2023) 
gameData = entry.split('\n')
# game'leri ayırmak 
sum=0 
           
for i in range(len(gameData)):
    # i for indexing games, i+1 = game id
    # 12 red cubes, 13 green cubes, and 14 blue cubes 
    # data is a string of an only game
    gameId = i+1
    data = gameData[i]   
    color = ["red","green","blue"]
    limit = [12,13,14] 
    isFaulty = False
    for j in range(len(color)):
        pattern = "([\d*]+) {}".format(color[j])
        neededInfo= re.findall(pattern,data) 
        for k in range(len(neededInfo)): 
            if (int(neededInfo[k]) > limit[j]) & (isFaulty==False):
                print("Game {} is faulty!".format(gameId)) 
                isFaulty=True
                break
    if isFaulty==False:
        print("Game {} is NOT faulty!".format(gameId))
        sum = sum + gameId 
print("sum= ",sum)

            


        
