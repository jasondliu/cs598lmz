import mmap
import os
import sys
import time
from random import randint
from random import shuffle

from scapy.all import *

# TODO:
#   * Check if this is really needed
#   * Add support for more filetypes

# Reads a file into a list of strings
def readFile(filepath):
    file = open(filepath, "r")
    lines = file.readlines()
    file.close()
    shuffle(lines)
    return lines

# Reads a file into a list of integers
def readIntFile(filepath):
    file = open(filepath, "r")
    lines = file.readlines()
    file.close()
    return [int(line) for line in lines]

# Reads a file into a list of integers
def readIntFile(filepath, shuffle=False):
    file = open(filepath, "r")
    lines = file.readlines()
    file.close()
    lines = [int(line) for line in lines]
    if shuffle:
        shuffle(lines)
    return lines

