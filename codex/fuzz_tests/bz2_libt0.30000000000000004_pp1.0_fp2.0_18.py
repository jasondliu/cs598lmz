import bz2
bz2.BZ2File(path)

# read the entire file into a single byte string
with open(path, 'rb') as f:
    data = f.read()

# decompress the data
data = bz2.decompress(data)

# write the data out to a file
with open('baby1990.html', 'wb') as f:
    f.write(data)

# parse the HTML file into a DOM tree
from bs4 import BeautifulSoup
dom = BeautifulSoup(data)

# extract the text from the DOM tree
dom.get_text()

# find all the occurrences of the word "the"
import re
re.findall(r'the', dom.get_text())

# find all the occurrences of the word "the"
import re
re.findall(r'\bthe\b', dom.get_text())

# find all the occurrences of the word "the"
import re
re.findall(r'\b[Tt]he\b', dom.get_text())

# find all the occurrences of
