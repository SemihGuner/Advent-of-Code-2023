# https://pypi.org/project/advent-of-code-data/
import aocd
entry = aocd.get_data(day=1,year=2023) 
spData = entry.split('\n')

toplam = 0
numbers = ["one","two","three","four","five","six","seven","eight","nine"] 
for i in range(len(spData)):
    #print("start of i")
    yeniStr="0"
    # Part 1 
    for j in range(len(spData[i])):
        #print("start of j")
        if spData[i][j].isdigit():
            yeniStr += spData[i][j]
            print("i-j: {}-{}".format(i,j)) 
        else:
            # Part 2  
            araniyor=""
            check = True
            for p in range(len(numbers)): 
                #print("start of p")
                numLen = len(numbers[p]) 
                araniyor = spData[i][j:j+numLen]
                print("i-j-p: {}-{}-{} ; araniyor: {} ; numLen: {}".format(i,j,p,araniyor,numLen)) 
                if (araniyor == numbers[0]) & check:
                    yeniStr+="1"
                    print("Gotcha! YeniStr= " , yeniStr)  
                    check=False
                elif (araniyor == numbers[1]) & check:
                    yeniStr+="2"
                    print("Gotcha! YeniStr= " , yeniStr)   
                    check=False
                elif (araniyor == numbers[2]) & check:
                    yeniStr+="3"
                    print("Gotcha! YeniStr= " , yeniStr)   
                    check=False
                elif (araniyor == numbers[3]) & check:
                    yeniStr+="4"
                    print("Gotcha! YeniStr= " , yeniStr)   
                    check=False
                elif (araniyor == numbers[4]) & check:
                    yeniStr+="5"
                    print("Gotcha! YeniStr= " , yeniStr)   
                    check=False
                elif (araniyor == numbers[5]) & check:
                    yeniStr+="6"
                    print("Gotcha! YeniStr= " , yeniStr)   
                    check=False
                elif (araniyor == numbers[6]) & check:
                    yeniStr+="7"
                    print("Gotcha! YeniStr= " , yeniStr)   
                    check=False
                elif (araniyor == numbers[7]) & check:
                    yeniStr+="8"
                    print("Gotcha! YeniStr= " , yeniStr)   
                    check=False
                elif (araniyor == numbers[8]) & check:
                    yeniStr+="9"
                    print("Gotcha! YeniStr= " , yeniStr)   
                    check=False
    donusecekStr = yeniStr[1] + yeniStr[-1]
    toplam+=int(donusecekStr) 
print("Summation:" , toplam)
