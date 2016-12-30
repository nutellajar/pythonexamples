#!/usr/bin/python
from __future__ import division
from collections import Counter

import sys

num_of_integers = int(raw_input("enter number of integers:"))
list_of_integers = []

for x in range(num_of_integers):
    myinput = int(raw_input("Enter a number: "))
    list_of_integers.append(myinput)
    print x

sortedlist = sorted(list_of_integers)

print "how many integers", num_of_integers
print "list of integers", list_of_integers
print "sorted list", sortedlist
data = Counter(sortedlist)
print "Mode : ", data.most_common(1)

print "Mean" , sum(list_of_integers) / len(list_of_integers)
if (len(list_of_integers)%2 == 1):
    print "Median 0 ", sortedlist[int(len(sortedlist)/2)]
else:
    m = sortedlist[int(len(sortedlist)/2) -1 ]
    n = sortedlist[int((len(sortedlist)/2))]
    median1 = (m+n)/2
    print "Median : %0.2f" % (median1)
