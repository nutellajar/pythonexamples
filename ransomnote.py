#!/usr/bin/python
# Ransom note
import os
import string
import collections

def generateRansomNote(rnote, magazine):

    #exclude = set(string.punctuation)
    magCounter = collections.Counter()
    striprnote = ''.join(rnote.split()).lower()
    noteCounter = collections.Counter(striprnote)
    print noteCounter

    if len(rnote) > os.path.getsize(magazine):
        print "Note is longer Magazine"
        return False
    with open(magazine) as mag:
        for pattern in mag:
            pattern = ''.join(pattern.split()).lower()
            #print pattern
            #s = ''.join(ch for ch in pattern if ch not in exclude)
            magCounter.update(pattern)

    for n in striprnote:
        print ":" , n
        if magCounter[n] == 0:
            print "Missing letter %s from magazine, cannot produce ransom note" % n
            return False
        else:
            magCounter[n] -= 1
    print "Success"
    return True






ransomnote = "please deliver $20 dollars"
magazinetxt = "magsample.txt"
generateRansomNote(ransomnote,magazinetxt)
