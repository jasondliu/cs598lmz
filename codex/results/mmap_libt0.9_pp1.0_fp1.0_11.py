import mmap
import sys
import multiprocessing as mp
import matplotlib.pyplot as plt
import re

def map_func(line):
    line = line.split(' ')
    if len(line) == 9:
        try:
            data = map(int, line[1:7]) + map(float, line[7:])
            data = map(str, data)
            return  ','.join(data)
        except:
            return None

def reduce_func(arr):
    return len(arr)

def partition_func(label, k):
    return label % k

def open_file(filename):
    with open(filename) as f:
        return f.readlines()

def hash_func(data, k):
    for i in range(0, k):
        if i == data[-1] % k:
            return data
    return None

def batch_map_function(line):
    data = line[:-1].split(',')
    data[-1] = float(data[-1]) - float
