from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(comp)


# In[ ]:


# Problem 2 - Decode the file

import sys
import bz2


comp = bz2.BZ2File('file.bz2', 'r')
file = open('file.txt', 'w')

for line in comp:
    file.write(line)

file.close()
comp.close()


# In[ ]:


# Problem 3 - Extract the file

import tarfile
tar = tarfile.open('file.tar')
tar.extractall()
tar.close()


# In[ ]:


# Problem 4 - Decode the file

import fileinput

for line in fileinput.input('file.txt', inplace=True):
    line = line.replace(' ', '\n')
    sys.stdout.write(line)


# In[ ]:


# Problem 5 - Sort the data

import sys

for line in sys.stdin:
    print(line.strip())
