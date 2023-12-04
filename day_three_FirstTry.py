# https://pypi.org/project/advent-of-code-data/
import aocd 
from aocd import submit 
import re 
import numpy as np

entry = aocd.get_data(day=3,year=2023) 
engineData = entry.split('\n')


def generate_unique_list(pattern, data):
    unique_list = []

    for item in data:
        matches = re.findall(pattern, item)
        if matches:
            match_value = matches[0]
            if match_value not in unique_list:
                unique_list.append(match_value)

    unique_list.sort()
    return unique_list

def getIndexes(specialList, data):  
    ind= {}
    for i in range(len(data)):
        for j in range(len(data[i])):
            if (data[i][j] in specialList) & (j not in ind):
                ind[(i,j)] = data[i][j]
    #ind.sort()
    return ind 

def findNumberLocations(data,turnCount):
    totalNumandInd = {}
    i=0
    while i < turnCount:
        j=0
        while j < len(data[i]):  
            # Start checking indexes of the row.
            if j <= len(data[i])-3: #This if is to make sure we don't gat OutOfIndex error. Checks if we are still in the array.
                if data[i][j].isdigit() & data[i][j+1].isdigit() & data[i][j+2].isdigit():
                    #3 digit number
                    num = int(data[i][j])*100 + int(data[i][j+1]) * 10 + int(data[i][j+2]) 
                    totalNumandInd[(i,j)] = num
                    totalNumandInd[(i,j+1)] = num
                    totalNumandInd[(i,j+2)] = num
                    j+=3
                    
                elif data[i][j].isdigit() & data[i][j+1].isdigit():
                    #2 digit number
                    num = int(data[i][j])*10 + int(data[i][j+1]) 
                    totalNumandInd[(i,j)] = num
                    totalNumandInd[(i,j+1)] = num
                    j+=2
                    
                elif data[i][j].isdigit():
                    num = int(data[i][j])
                    totalNumandInd[(i,j)] = num 
                    j+=1
                    
            elif j <= len(data[i])-2: #This if is to make sure we don't gat OutOfIndex error. Checks if we are still in the array.
                if data[i][j].isdigit() & data[i][j+1].isdigit():
                    #2 digit number
                    num = int(data[i][j])*10 + int(data[i][j+1]) 
                    totalNumandInd[(i,j)] = num
                    totalNumandInd[(i,j+1)] = num
                    j+=2
                    
                elif data[i][j].isdigit():
                    num = int(data[i][j])
                    totalNumandInd[(i,j)] = num 
                    j+=1
                    
            elif j<=len(data[i])-1: #This if is to make sure we don't gat OutOfIndex error. Checks if we are still in the array.
                if data[i][j].isdigit():
                    num = int(data[i][j])
                    totalNumandInd[(i,j)] = num 
                    j+=1
                    
            j+=1

        i+=1
    return totalNumandInd

def SpotTheMarkedNumbers(numberDict, specialDict,specialList):
    summation = 0
    # dikey | 
    for key,value in numberDict.items():
        alreadySummed = False
        holdKey = key[1]
        for tKey, tValue in specialDict.items():  
            if (tKey[1] == holdKey) and (not alreadySummed): 
                summation += int(value)
                print(f"Adding {value} to summation")
                break

    # yatay |
    for yKey,yValue in numberDict.items():
        if (yKey[0]-1 in specialList) & (yKey[0]+1 in specialList):
            summation+= yValue

    return summation


# definitions end here, and cmds start.
specials= generate_unique_list("[^0-9.]",entry)
indexesOfSpecials= getIndexes(specials,engineData) 
NumsAndIndexes = findNumberLocations(engineData, len(engineData)) 
spots = SpotTheMarkedNumbers(NumsAndIndexes,indexesOfSpecials,specials)
#print(indexesOfSpecials)
print("spots:" , spots)
