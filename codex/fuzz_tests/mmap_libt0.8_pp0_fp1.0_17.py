import mmap
import os
from itertools import chain
from PIL import Image

def read_lines(filename):
    fd = open(filename)
    mm = mmap.mmap(fd.fileno(), 0, prot=mmap.PROT_READ)
    lines = mm.readlines()
    mm.close()
    fd.close()
    return lines

def parse_line(line):
    '''Returns an array of floating point features'''
    return chain.from_iterable(map(lambda x: list(map(float, x.split(':'))[1:]),
                                   line[3:].split()))

def read_lines_with_index(filename):
    lines = read_lines(filename)
    return [(int(line[0]), parse_line(line)) for line in lines]

def create_data_matrix(lines):
    '''Returns a numpy array of features'''
    new_lines = []
    for line in lines:
        new_lines.append(line[1])
    return np.array(new
