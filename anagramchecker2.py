#!/usr/bin/python

from collections import defaultdict

word_anagrams = defaultdict(set)

with open('words3.txt') as dictionary:
   for word in dictionary:
      word = word.rstrip()

      word_anagrams[''.join(sorted(word))].add(word)

num_cases = int(raw_input("Input number of words needed to be unscrambled: "))

num_matched_anagrams = 1
while num_matched_anagrams <= num_cases:
   scrambled_word = raw_input("Input scrambled word: ")
   sorted_word = ''.join(sorted(scrambled_word))

   if word_anagrams[sorted_word]:
      for word in word_anagrams[sorted_word]:
         print "Possible Word for Scrambled Word #" + str(num_matched_anagrams) + ": " + word

   else:
      print "No matches found"

   num_matched_anagrams += 1
