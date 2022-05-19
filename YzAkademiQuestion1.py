a = []
b = []
returnArray=[]
aPoints=0
bPoints=0

for i in range (3):
    a.append(int (input('Alice > ')))

for i in range (3):
    b.append(int(input('Bob > ')))

for i in range (3):
    if (a[i]>b[i]):
        aPoints+=1
    elif (b[i]>a[i]):
        bPoints+=1

returnArray.append(aPoints)
returnArray.append(bPoints)

print(returnArray)