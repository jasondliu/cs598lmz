import mmap
import re
import os

def load_data(filename, log_file="data.log"):
    """
    load data from file and return as list of strings
    """

    log = open(log_file, "a")
    print("Loading data from: " + filename)
    log.write("Loading data from: " + filename + "\n")
    data = []
    with open(filename, "r") as f:
        for line in f:
            if line.strip():
                data.append(line.strip())
    print("Done")
    log.write("Done\n")
    log.close()
    return data

def find_substring(substring, string):
    """
    return a list of indices where substring is found in string
    """
    indices = []
    index = 0
    while True:
        index = string.find(substring, index)
        if index == -1:
            break
        else:
            indices.append(index)
            index += 1
    return indices

