#!/Users/prachishah/anaconda3/bin/python

from operator import itemgetter
import sys

current_word = None
current_count = 0

#this dictionary stores all the words and their frequencies
#it will later be used to extarct top words based on application(Word cloud or Co-occurence)
topWords = {}   
#this dictionary stores the frequency of words in ascending order
sort = {}

#input is taken from stdin
for line in sys.stdin:
    line = line.strip()

    #splits the mapper input
    word, count = line.split(' ',1)
    try:
        count = int(count)
    except ValueError:
        continue

    #this sums the mapper input to calculate the WordCount
    if current_word == word:
        current_count += count
    else:
        if current_word:
            #this print stmt given the final wordCount frequency in part-0000(R-1) file
            #print ('%s %s' % (current_word, current_count))    
            topWords[current_word] = current_count
        #these stmts execute when new word comes as input
        current_count = count
        current_word = word

if current_word == word:
    #print ('%s %s' % (current_word, current_count))
    topWords[current_word] = current_count

import operator
length = len(topWords) - 1
#this sorts all the words in ascending order
sortedWords = sorted(topWords.items(), key=operator.itemgetter(1))

'''
#these stmt prepare intermediate files for producing co-occurence application
with open('/Users/prachishah/Desktop/WordCount/scripts/temp.txt', 'w', newline = '') as f:
    for i in range(10):
        #print(sortedWords[length - i][0]+'\t'+str(sortedWords[length -i][1]))
        #this stmt writes top 10 words
        f.write(sortedWords[length - i][0])
        if i < 9:
            f.write(' ')

#these lines emit output for normal WordCount Problem
for x,y in topWords.items():
    print(x+'\t'+str(y))

'''

#the following stmts are used to produce output for WordCloud application
for i in range(100):
    sort[sortedWords[length - i][0]] = sortedWords[length -i][1]

import csv 

with open('/Users/prachishah/Desktop/WordCount/output/cloudArticlesDay.csv', 'w', newline = '') as f:
    w = csv.writer(f)
    w.writerow(['text','size'])
    for key, value in sort.items():
       w.writerow([key, value])



