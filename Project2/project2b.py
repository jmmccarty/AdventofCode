valid=0

# read in the file
file1 = open('input.txt', 'r') 
Lines = file1.readlines() 

#split the line and check if password is valid
for line in Lines:
    l=line.split()
    l2=l[0].split("-")
    pw=l[2]
    pos1=int(l2[0])-1
    pos2=int(l2[1])-1
    letter=l[1].strip(":")
    char1=pw[pos1]
    char2=pw[pos2]
    if char1 == letter:
        if char2 == letter:
            print('Password is invalid')
        else:
            valid=valid+1
    elif char2 == letter:
        valid=valid+1
    else:
        print("Password is invalid")
print(valid)






