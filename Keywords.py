# This is the keywords that are input into the system set as a vector
import math
import numpy as np
from database import *


# should accept the keywords input and output the corresponding vector with the keyword
def keywordIn(word):
    index = 0
    found = False
    kvector = keywordVector()  # should be a 1x108 list containing the keywords from the database
    kMatrix = kpMatrix()  # should be the 108x30 matrix containing points which correspond with the keywords and
    # protocols
    # loops until keyword is found
    while not found:
        if word == kvector[index]:
            found = True
        elif index > len(kvector) - 2:
            # output nothing, needs to communicate to devs that keyword was not found
            found = True
        else:
            index += 1
    # out of loop
    vec = kMatrix[index]  # outputs the i-th row from the kp-Matrix
    return vec


# takes in the combination vector as an input and outputs the maximum values index
def maxVal(vector):
    arrMax = [0]  # stores the maximum value in the vector
    maxi = np.array([0])  # stores the index of the maximum value in the vector
    for index in range(len(vector)):  # algorithm finds the max value and corresponding index in the array
        if len(arrMax) > 1 and vector[index] > arrMax[0]:
            np.delete(maxi)  # removes all the elements from the maximum index values vector
            maxi[0] = index
            arrMax.append(vector[index])
        elif math.ceil(vector[index]) > arrMax[0]:
            maxi[0] = index
            arrMax.append(vector[index])
        elif vector[index] == arrMax[0]:
            np.append(maxi, index)  # adds the index of the equal max value index
    return maxi  # outputs the index of the largest value


# accepts the index of the maximum value and outputs the policy associated with that value
def protocol(index):
    vec = protocolVector()  # an example, the vector will have all 30+ policies from the logic sheet
    plist = []
    for i in index:
        plist.append(vec[i])
    return plist


# gets the index of a protocol
def protocolIndex(word):
    index = 0
    vec = protocolVector()  # gets the keyword vector from the database
    found = False
    while found:
        if word == vec[index]:
            found = True
        elif index >= vec.len():
            # output a message to mods about a missing keyword
            found = True
            index = 0
        else:
            index += 1
    return index


# gets the index of a specified keyword
def keywordIndex(word):
    index = 0
    vec = keywordVector()  # gets the keyword vector from the database
    found = False
    while found:
        if word == vec[index]:
            found = True
        elif index >= vec.len():
            # output a message to mods about a missing keyword
            found = True
            index = 0
        else:
            index += 1
    return index


# checks is protocol was accepted and gives the algorithm a reward or punishment depending
def accepted(answer, llist, pcol):
    if answer:
        reward(llist, pcol)
    else:
        punishment(llist, pcol)


# defines the reward function
def reward(llist, pcol):
    prop = rVal(llist, pcol)
    for i in range(len(llist)):
        vec = keywordIn(llist[i])
        kIn = protocolIndex(pcol)
        vec[kIn] += vec[kIn] / prop
    print(vec)


# defines the reward function
def punishment(llist, pcol):
    prop = rVal(llist, pcol)
    for i in range(len(llist)):
        vec = keywordIn(llist[i])
        kIn = keywordIn(pcol)
        vec[kIn] -= vec[kIn] / prop


# this one has problems
def rVal(llist, pcol):
    summant = 0
    print(llist)
    print(pcol)
    for i in range(len(llist)):
        vec = keywordIn(llist[i])
        print(vec[pcol])
        summant += vec[pcol]
    print(summant)
    return summant
