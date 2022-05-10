import bz2
bz2_file = bz2.BZ2File('unzipped.txt.bz2')
for line in bz2_file:
    words = line.split()
    for word in words:
        if word.isalpha():
            data.append(word.lower())
data[:10]

def read_file(file):
    """Given a bz2 compressed file path, return a list of
    words in the file.
    """
    with bz2.BZ2File(file, 'r') as f:
        data = f.read().decode('utf-8')
    return data.split()

file = 'unzipped.txt.bz2'
read_file(file)[:10]

# Quiz: CSV Reader
import csv
f = open('mpg.csv')
mpg = list(csv.DictReader(f))

mpg[:3]

mpg[0].keys()

sum(float(d['cty']) for d in mpg) / len(mpg)

sum(float
