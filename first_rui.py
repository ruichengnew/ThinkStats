import survey

table = survey.Pregnancies()
table.ReadRecords()
print('Number of pregnancires', len(table.records))

def Outcome():
    count = 0
    for var in table.records:
        if var.outcome == 1:
            count += 1
    return count

print("Number of babies: ", Outcome())

def BirthOrd():
    firstbaby = 0
    otherbaby = 0
    for var in table.records:
        if var.birthord == 1:
            firstbaby += 1
        elif var.birthord != 1 and str(var.birthord).isdigit():
            otherbaby += 1
        else:
            pass
    return firstbaby, otherbaby

print("Number of firstbaby: ", BirthOrd()[0])
print("Number of otherbaby: ", BirthOrd()[1])

def PregLength():
    firstbabylength = []
    otherbabylength = []
    for var in table.records:
        if var.birthord == 1:
            firstbabylength.append(var.prglength)
        elif var.birthord != 1 and str(var.birthord).isdigit():
            otherbabylength.append(var.prglength)
        else:
            pass
    return firstbabylength, otherbabylength

def Mean(LIST):
    return sum(LIST)/len(LIST)

print("Mean of firstbaby prglength:", Mean(PregLength()[0]))
print("Mean of otherbaby prglength:", Mean(PregLength()[1]))
print("The prglength differnece between firstbaby and otherbaby in weeks:", (Mean(PregLength()[0]) - Mean(PregLength()[1])))
