import mmap
import re
import os
import sys
import time
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc

def find_all(a_str, sub):
    start = 0
    while True:
        start = a_str.find(sub, start)
        if start == -1: return
        yield start
        start += len(sub) # use start += 1 to find overlapping matches

def find_all_index(a_str, sub):
    start = 0
    while True:
        start = a_str.find(sub, start)
        if start == -1: return
        yield start
        start += len(sub) # use start += 1 to find overlapping matches

def find_all_index_from_list(a_str, sub_list):
    start = 0
    index_list = []
    for sub in sub_list:
        start = 0
        while True:
            start = a_str.find(sub, start)
            if start == -1: break
            index_list.append(
