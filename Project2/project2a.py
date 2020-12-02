valid=0

# read in the file
file1 = open('input.txt', 'r') 
Lines = file1.readlines() 

#split the line and check if password is valid
for line in Lines:
    l=line.split()
    l2=l[0].split("-")
    min=int(l2[0])
    max=int(l2[1])
    letter=l[1].strip(":")
    total=int(l[2].count(letter))
    if min <= total <= max:
        valid=valid+1
print(valid)






