import bz2
# Test BZ2Decompressor
# https://stackoverflow.com/questions/2695152/how-to-decompress-bz2-files-in-python

bz2_file = bz2.BZ2File('../data/train.ft.txt.bz2')
data = bz2_file.read()

# for line in bz2_file:
#     print(line)
bz2_file.close()
len(data)

# -*- coding: utf-8 -*-
"""
Created on Wed Oct  3 12:31:06 2018

@author: Zobair
"""

import bz2
import re

def main():
    # Open the compressed file
    file = bz2.BZ2File('../data/train.ft.txt.bz2')
    # Create a new file in which to write the decompressed data
    data = file.read()
    # Decompress the data
    # ...
    # Write the decompressed data
    # ...
    # Close the files
    file.close()
   
