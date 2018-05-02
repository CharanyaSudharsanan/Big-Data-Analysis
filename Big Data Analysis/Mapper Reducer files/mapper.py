#!/Users/prachishah/anaconda3/bin/python
"""mapper.py"""

import sys
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into words
    words = line.split()
    #NLTK package helps to remove common englsh words
    stop_words = set(stopwords.words('english'))
    # increase counters
    for word in words:
        if not word in stop_words:
            #this condition is used to remove other common
            #words which are not removed by NLTK
            if len(word) > 4:
                #this is the output that Mapper emits to Reducer
                print (word, ' ', 1)
