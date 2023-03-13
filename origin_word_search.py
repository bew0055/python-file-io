#!/bin/python3

# Words to look for: inherit, inheritance, heritable, and other forms of these words - including both upper and lower case

import re
import sys

# r' - used so backslashes indicate a special character
# (?i) - indicates the regex search will be case insensitive 
# .. - matches any character for two characters
# herit - the literal characters herit
# \w+ - matches one or more word characters afetr herit

s = r'(?i)..herit\w+'
o = re.compile(s)

print('open origin.txt')
with open('origin.txt', 'r') as in_stream:
	print('open found_words.txt')
	with open('found_words.txt','w') as out_stream:
		word_line = 1
		for line in in_stream:
			line = line.strip()
			word_list = line.split()
			if o.search(line):
				word = o.search(line)
				print(word_line, "\t", word.group(), file = out_stream)
			word_line += 1
print("done")
print('origin.txt is closed?', in_stream.closed)
print('found_words.txt is closed?', out_stream.closed)

