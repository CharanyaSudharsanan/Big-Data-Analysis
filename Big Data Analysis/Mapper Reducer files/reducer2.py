#!/Users/prachishah/anaconda3/bin/python

from operator import itemgetter
import sys

current_word = None 	#one of the top 10 words
current_list = []	#this list is used to store co-occuring words with current_Word

for line in sys.stdin:
	line = line.strip()
	word, coword = line.split(' ')
	

	if current_word == word and len(coword) > 4:
		if coword not in current_list:
			current_list.append(coword)
	else:
		if current_word:
			print(current_word,current_list)
		current_list = []
		current_list.append(coword)
		current_word = word

if current_word == word:
	#this outputs the final co-occuring words list for the top 10 words 
	print(current_word,list(set(current_list)))
	sys.stdout.flush()

