#!/usr/bin/python

"""

Problem: Given a sequence of nonnegative integers A and an integer T, return whether there is a *continuous sequence* of A that sums up to exactly T

Example
[23, 5, 4, 7, 2, 11], 20. Return True because 7 + 2 + 11 = 20
[1, 3, 5, 23, 2], 8. Return True because 3 + 5 = 8
[1, 3, 5, 23, 2], 7 Return False because no sequence in this array adds up to 7

Note: We are looking for an O(N) solution. There is an obvious O(N^2) solution which is a good starting point but is not the final solution we are looking for.

"""



def FindSum(A, T):
    queueSum = []
    for i in A:
        queueSum.append(i)
        while sum(queueSum) > T:
            queueSum.pop(0)
        if sum(queueSum) == T:
            return True
    return False

alist = [23, 5, 4, 7, 2, 11]
print FindSum(alist, 20)

blist = [1, 3, 5, 23, 2]

print FindSum(blist, 10)

print FindSum(blist, 7)
