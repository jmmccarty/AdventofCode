# Using readlines() 
file1 = open('input.txt', 'r') 
Lines = file1.readlines() 
  
count = 0
valueDict = {}
# Strips the newline character 
for line in Lines: 
    valueDict[count] = line.strip()
    count=count+1
values=count
print(valueDict)
total = 0
  
for i in valueDict:
    value1=int(valueDict[i])
    for z in valueDict:
        value2=int(valueDict[z])
        total=value1+value2
        if total ==2020:
            print(value1, value2, total)
            newtotal = value1 * value2
            print (newtotal)

            

