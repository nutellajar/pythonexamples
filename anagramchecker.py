#!/usr/bin/python
# Check for Anagrams
import string
from collections import deque


def checkAnagrams(s, t):
    if sorted(s.lower()) == sorted(t.lower()) :
        result = "True for %s %s" % (s,t)
    else:
        result = "False for %s %s" % (s,t)
    print result
    return 1

#checkAnagrams('creative', 'reactive' )
#checkAnagrams('Silent', 'Listen')
#checkAnagrams('house', 'mouse')

def isSentenceAnagram(sentence):
    exclude = set(string.punctuation)
    s2 = ''.join(ch for ch in sentence if ch not in exclude)
    s3 = s2.replace(" ","")
    print s3 + "\n"
    ds = deque(s3.lower())

    while ds:
        if ds.popleft() != ds.pop():
            return False
        elif len(ds) == 1 and len(sentence) > 0 :
            return True
    return True

print "Noel sees Leon." , isSentenceAnagram("Noel sees Leon.")
print "Mother Eve's noose we soon sever, eh, Tom?" , isSentenceAnagram("Mother Eve's noose we soon sever, eh, Tom?")
