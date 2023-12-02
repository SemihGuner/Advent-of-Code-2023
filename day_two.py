# https://pypi.org/project/advent-of-code-data/
import aocd
import re
entry = aocd.get_data(day=2,year=2023) 
gameData = entry.split('\n')
# game'leri ayırmak 
sum=0

for i in range(len(gameData)):
    # i for indexing games, i+1 = game id
    # 12 red cubes, 13 green cubes, and 14 blue cubes
    countofR=0
    countofG=0
    countofB=0
    data = gameData[i] 
    pattern = "[0-9]+\s[greenredblue]+;?"
    neededInfo= re.findall(pattern,data)
    printedOnce = False
    pulls=0
    for j in range(len(neededInfo)):
        if neededInfo[j].find("green") != -1:
            patternTwo = "[0-9]+"
            neededTwo = re.findall(patternTwo,neededInfo[j])
            countofG+= int(neededTwo[0])
            #print("in i ->",i+1," , ", countofR," , ",countofG," , ",countofB," , ")
            if neededInfo[j].find(";") !=  -1 | ((neededInfo[j] == neededInfo[-1]) & pulls==2):  
                pulls+=1 
                #print("in j ->",i+1," , ", countofR," , ",countofG," , ",countofB," , ") 
                if ((countofR > 12) | (countofG > 13) | (countofB > 14)) & (printedOnce==False):
                    printedOnce=True
                    print("Game {} is faulty!".format(i+1))    
            elif printedOnce==False & pulls==2:
                sum= sum+i+1
                print("Game {} is NOT faulty!".format(i+1))
            countofR=0
            countofG=0
            countofB=0 
        elif neededInfo[j].find("red") != -1:
            patternTwo = "[0-9]+"
            neededTwo = re.findall(patternTwo,neededInfo[j])
            countofR+= int(neededTwo[0])
            #print("in i ->",i+1," , ", countofR," , ",countofG," , ",countofB," , ")
            if neededInfo[j].find(";") !=  -1 | ((neededInfo[j] == neededInfo[-1]) & pulls==2): 
                pulls+=1 
                #print("in j ->",i+1," , ", countofR," , ",countofG," , ",countofB," , ") 
                if ((countofR > 12) | (countofG > 13) | (countofB > 14)) & (printedOnce==False):
                    printedOnce=True
                    print("Game {} is faulty!".format(i+1))    
            elif printedOnce==False & pulls==2:
                sum= sum+i+1
                print("Game {} is NOT faulty!".format(i+1))
            countofR=0
            countofG=0
            countofB=0 
        elif neededInfo[j].find("blue") != -1:
            patternTwo = "[0-9]+"
            neededTwo = re.findall(patternTwo,neededInfo[j])
            countofB+= int(neededTwo[0])
            #print("in i ->",i+1," , ", countofR," , ",countofG," , ",countofB," , ")
            if neededInfo[j].find(";") !=  -1 | ((neededInfo[j] == neededInfo[-1]) & pulls==2): 
                pulls+=1 
                #print("in j ->",i+1," , ", countofR," , ",countofG," , ",countofB," , ") 
                if ((countofR > 12) | (countofG > 13) | (countofB > 14)) & (printedOnce==False):
                    printedOnce=True
                    print("Game {} is faulty!".format(i+1))  
            elif printedOnce==False & pulls==2:
                sum= sum+i+1
                print("Game {} is NOT faulty!".format(i+1))
            countofR=0
            countofG=0
            countofB=0 

print(sum)

            


        
