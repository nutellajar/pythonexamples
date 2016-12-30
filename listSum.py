#!/usr/bin/python
# Given a list of integers and a sum, find the pairs that add up to that sum
"""
[1,5,3,6,10,11] , 9  returns True  (3,6)
[1,2,5,6,0,9,10,4], 6  returns True ( 1,5), (6,0)
[3,4,5,1,7,8,9,2,3,6], 10 returns True (3,7), (6,4)


"""

def listSum(listintegers, sum):
    sortedList = sorted(set(listintegers))
    foundPair = False
    for x in sortedList:
        if x in listintegers:
            listintegers.remove(x)
            if (sum - x) in listintegers:
                print "Found pair : (%d , %d) for sum:%d " % (x,sum-x, sum)
                foundPair = True
                listintegers.remove(sum-x)
    if not foundPair:
        print "No pairs for sum: %d " % sum


# Given a list of integers and a sum, find the pairs that add up to a difference
"""
[1,5,3,6,10,11] , 3  returns True  (3,6)
[1,2,5,6,0,9,10,4], 4  returns True ( 1,5), (6,2)
[3,4,5,1,7,8,9,2,3,6], 6 returns True (3,9), (8,2), (7,1)


"""

def listDiff(listintegers, diff):
    sortedList = sorted(set(listintegers), reverse=True)
    foundPair = False
    for x in sortedList:
        if x in listintegers:
            listintegers.remove(x)
            if (x - diff) in listintegers:
                print "Found pair : (%d , %d) for difference:%d " % (x,x-diff, diff)
                foundPair = True
                listintegers.remove(x-diff)
    if not foundPair:
        print "No pairs for difference: %d " % diff




list1 = [3,4,5,1,7,8,9,2,3,6,0]
l = [1,5,3,6,10,11,5,4,2,7,0,9]
listSum(l, 9)

list2 = [3,4,5,1,7,8,9,2,3,6,0,5,10]

listDiff(list2,5)
