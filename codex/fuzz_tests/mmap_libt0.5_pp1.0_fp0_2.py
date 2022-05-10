import mmap
import os
import sys
import time
import re

# Read in the file
#f = open('/Users/charles/Desktop/repos/data/test.txt', 'r')
f = open('/Users/charles/Desktop/repos/data/test.txt', 'r')
# Instantiate the class
p = pdftotext(f)
# Get the text as a list of pages
pages = p.get_pages()
# Get the text as a list of lines
lines = p.get_lines()

# Print the text
print(pages)
print(lines)

# Close the file
f.close()

# Read in the file
#f = open('/Users/charles/Desktop/repos/data/test.txt', 'r')
f = open('/Users/charles/Desktop/repos/data/test.txt', 'r')
# Instantiate the class
p = pdftotext(f)
# Get the text as a list of pages
pages = p.get_pages()
# Get the text as a list of
