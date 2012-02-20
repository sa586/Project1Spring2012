# Filename: MakeVecFile.py

from decimal import *

#### readfile to get the list of CA
f = open('list.txt', 'r')
sequenceCA = {}
sequence = 1
listCA = {}

while True:
    line = f.readline()
    if len(line)==0:
        break
    else:
        keys = line.split("\"")
        listName = str(keys[1]).strip()
        #print listName
        ###### make a dictionary key: value = (CA name : # of article)
        sequenceCA[sequence] = str(listName).lower()
        listCA[str(listName).lower()] = 0
        sequence += 1
f.close()

#for key, value in listCA.items():
#    print key + ":" + str(value)

#for key, value in sequenceCA.items():
#    print str(key) + ":" + value

####### read in.txt to save the # of article to each CA
f = open('in2.txt', 'r')
totalarticle = 0
while True:
    line = f.readline()
    if len(line) == 0:
        break
    else:
        if len(line.partition(" ")[0]) == 2:
            CurrentIndex = line.partition(" ")[0]
            if CurrentIndex == 'ID':
                totalarticle += 1
            #print CurrentIndex
            if CurrentIndex == 'CA':
                #print str(line.partition(" ")[2]).strip()
                field = str(line.partition(" ")[2]).strip()
                if field.lower() in listCA:
                    listCA[field.lower()] = listCA[field.lower()] + 1
f.close()
#for key, value in listCA.items():
#    print key + ":" + str(value)

#### make vec file

f = open('static2.vec', 'w')

f.write("\n")
f.write("*Vertices " + str(sequence-1) + "\n")
count = 1
print totalarticle
for key, value in sequenceCA.items():
    getcontext().prec = 8
    n = Decimal(listCA[value])/Decimal(totalarticle)
    print n
    f. write(str(n) + "\n")
    #f.write(str(listCA[value]) + "\n")
    #print str(listCA[value])
f.close()
