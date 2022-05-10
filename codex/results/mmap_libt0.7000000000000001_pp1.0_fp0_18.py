import mmap as mm
import numpy as np
import time
import random

t0 = time.time()
def get_lines(filename):
    fp = open(filename, "r+")
    buf = mm.mmap(fp.fileno(), 0)
    lines = 0
    readline = buf.readline
    while readline():
        lines += 1
    return lines

lines_1 = get_lines("./../data/test1.txt")
lines_2 = get_lines("./../data/test2.txt")

if(lines_1 != lines_2):
    print("Error: the 2 files have different number of lines")
else:
    total_lines = lines_1
    print("Total number of lines in this file is " + str(total_lines))
    random_lines = random.sample(range(1, total_lines), int(total_lines/20))
    random_lines.sort()
    print("Random lines are: ")
    print(random_lines)
    print("Time used: " + str(time.time() -
