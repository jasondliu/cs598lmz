import bz2
bz2.BZ2File(filename)

# read in the data
with bz2.BZ2File(filename) as f:
    data = [x.decode('utf-8') for x in f.readlines()]

# print the first 10 lines
print(data[:10])

# import necessary packages
import re

def get_publishers(data):
    """
    Return all of the unique publishers in the data.
    """
    publishers = []
    for line in data:
        # split the line into a list of column values
        cols = line.split('\t')
        # extract the publisher
        publisher = cols[2]
        # check if publisher is already in the list
        if publisher not in publishers:
            # if not, append it to the list
            publishers.append(publisher)
    return publishers

def get_titles(data):
    """
    Return all of the unique titles in the data.
    """
    titles = []
    for line in data:
        # split the line into a list of column values

