import codecs
codecs.register_error('asciiIgnore', codecs.ascii.ignore_errors)
import os
import argparse
#nltk.download('punkt')
#nltk.download('stopwords')
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

# read the contents of a file in the format [word]:[id]
def loadWords(filename):
    words = {}
    wordsIgnore = {}
    f = codecs.open(filename,"r","asciiIgnore")
    lines = f.readlines()
    for line in lines:
        line = line.strip()
        parts = line.split(':')
        if len(parts) == 2:
            (word,id) = parts
            words[word] = int(id)
            wordsIgnore[word.lower()] = int(id)
    return (words,wordsIgnore)

# read the contents of a file in the format [id]:[word]
# the file is sorted
def loadWordsById(filename):
    words = {}

