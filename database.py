import csv

with open('Project Database.csv', 'rt') as f:  # accesses the database
    reader = csv.reader(f)
    data_as_list = list(reader)  # gets all the entries of the database as a list

protocolList = data_as_list[0]  # gets the list of all protocols
protocolList = protocolList[1:]  # removes the "keyword" element
rowSize = len(data_as_list)
colSize = len(data_as_list[0])

keywordList = []
for i in range(rowSize):  # iterates to get the keywords
    if i > 0:
        keywordList.append(data_as_list[i][0])

pointsMatrix = list(data_as_list[1:][0:])  # Gets the points with keywords
# pointsMatrix[0].remove(pointsMatrix[0][0])
for i in range(rowSize - 1):  # iterates to remove the keywords from the list
    pointsMatrix[i].remove(pointsMatrix[i][0])

for i in range(len(pointsMatrix)):  # iterates to cast each entry in the pointsMatrix to floating point numbers
    for j in range(len(pointsMatrix[i])):
        pointsMatrix[i][j] = float(pointsMatrix[i][j])


def keywordVector():
    return keywordList


def protocolVector():
    return protocolList


def kpMatrix():
    return pointsMatrix
