#!/usr/bin/python

def reduceString(s):
    stack2 = []
    s1 = list(s)
    print "Original string", s
    for i in range(len(s1)):
        if len(stack2) >= 1 :
            print "stack > 1", stack2
            print "i:", i
            if s1[i] == stack2[-1]:
                stack2.pop()
                print "after pop stack", stack2
            else:
                stack2.append(s1[i])
        else:
            stack2.append(s1[i])
    if len(stack2) == 0:
        print "Empty String"
    else:
        print "string", ''.join(stack2)


reduceString("g2ghheerrghg99")
