import mmap
import re
import sys
import time

import pymongo
from pymongo import MongoClient

import matplotlib.pylab as plt
import numpy as np

from collections import defaultdict

import pprint

pp = pprint.PrettyPrinter(indent=4)

#####

def get_memory_mapped_file(filename):
    return mmap.mmap(
        os.open(filename, os.O_RDONLY),
        0,
        access=mmap.ACCESS_READ)

#####

def get_file_stream(filename):
    return open(filename, "r")

#####

def get_file_stream_gen(filename):
    with open(filename, "r") as f:
        for line in f:
            yield(line)

#####

def get_file_stream_buffered_gen(filename):
    with open(filename, "r") as f:
        buffer = ""
        for line in f:
            buffer += line
            while "\n" in buffer
