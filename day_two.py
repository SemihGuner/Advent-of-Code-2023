# https://pypi.org/project/advent-of-code-data/
import aocd 
from aocd import submit
import re
entry = aocd.get_data(day=2,year=2023) 
gameData = entry.split('\n')
# game'leri ayırmak         
 
def partOne(): 
    color = ["red","green","blue"]
    limit = [12,13,14]
    sum=0    
    for i in range(len(gameData)):
        # i for indexing games, i+1 = game id
        # 12 red cubes, 13 green cubes, and 14 blue cubes 
        # data is a string of an only game
        gameId = i+1
        data = gameData[i]    
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
    print("part one: sum= ",sum)
    return sum 

#submit(partOne(),part="a",day=2,year=2023)

def partTwo():
    color = ["red","green","blue"]
    result=0
    for i in range(len(gameData)): 
        data = gameData[i]   
        highest=1
        for j in range(len(color)):
            pattern = "([\d]+) {}".format(color[j])
            neededInfo= re.findall(pattern,data) 
            temp=1
            for k in range(len(neededInfo)):  
                intIndex = int(neededInfo[k].strip()) 
                try:
                    if intIndex > temp:
                        temp = intIndex
                except Exception as err:
                    print("intIndex was {}".format(intIndex))
                    print("The error '{}' has been occured.".format(err))
                if k == len(neededInfo)-1: 
                    print("{}'s highest for gameId {} is: {}".format(color[j],i+1,temp))
                    highest = temp * highest
        print("highest for gameId {} is {}\n".format(i+1,highest))
        result += highest 
    print("result is:",result)
    return result

#submit(partTwo(),part="b",day=2,year=2023)

            


        
