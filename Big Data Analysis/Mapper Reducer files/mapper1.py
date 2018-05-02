#!/Users/prachishah/anaconda3/bin/python

import sys
import io


file = open("temp.txt",'r')
topwords = file.read().split(' ')
top = set(topwords)

for line in sys.stdin:
	line = line.strip()
	words = line.split()
	#'sets' has all the unique words in a tweet/article
	sets = set(words)
	#this statament checks if any of the top words exists in the current tweet/article
	common = list(sets.intersection(top))	

	#follwing statements emit pair of the following form
	#<one of the top 10 word, co-occuring word with the top 10 words>
	if common:
		for x in common:
			for y in sets:
				if( x != y):
					if(len(y) > 4):
						print(x+' '+y)