import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

import json

#File extensions
csvExtension = ".csv"
txtExtension = ".txt"

#File paths
dataPath = "data/"
lexFilePath = "data/lexicon.txt"
lexList = "data/lexlist/lexList.csv"

#Get line count
#https://stackoverflow.com/questions/845058/how-to-get-line-count-cheaply-in-python
def get_num_lines(file_path):
    fp = open(file_path, "r+")
    buf = mmap.mmap(fp.fileno(), 0)
    lines = 0
    while buf.readline():
        lines += 1
    return lines

#Array containing the lexicon
lexicon = []

#Word stemming (3rd party)
#https://github.com/amueller/word_cloud
p_stemmer = PorterStemmer()

#Function to handle word stemming

