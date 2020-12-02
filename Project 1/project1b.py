# Using readlines() 
file1 = open('input.txt', 'r') 
Lines = file1.readlines() 
  
count = 0
valueDict = {}
# Strips the newline character 
for line in Lines: 
    print("Line{}: {}".format(count, line.strip()))
    valueDict[count] = line.strip()
    count=count+1
values=count
print(valueDict)
total = 0
  
for i in valueDict:
    value1=int(valueDict[i])
    for z in valueDict:
        value2=int(valueDict[z])
        for x in valueDict:
            value3=int(valueDict[x])
            total=value1+value2+value3
            if total ==2020:
                print(value1, value2, total)
                newtotal = value1 * value2 * value3
                print (newtotal)

            

