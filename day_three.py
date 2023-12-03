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
    ind= np.array([], dtype=int)
    for i in range(len(data)):
        for j in range(len(data[i])):
            if (data[i][j] in specialList) & (j not in ind):
                ind = np.append(ind,j)
    ind.sort()
    return ind
specials= generate_unique_list("[^0-9.]",entry)
indexesOfSpecials= getIndexes(specials,engineData)

print(specials) 
print(indexesOfSpecials)
