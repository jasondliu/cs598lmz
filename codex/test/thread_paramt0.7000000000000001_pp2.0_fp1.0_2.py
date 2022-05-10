import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n' + ' ' * 9999)).start()

# from itertools import *
import math
from collections import *
from functools import *

with open('input.txt') as file:
    data = file.read()

lines = data.split('\n')
# lines = list(map(str.strip, lines))

inp = list(map(int, lines[0].split(',')))

inp[1] = 12
inp[2] = 2

def parse(data, i):
    op = data[i]
    if op == 99:
        return None, None, None, None
    elif op == 1:
        a, b, out = data[i+1 : i+4]
        return a, b, out, lambda x, y: x + y
    elif op == 2:
        a, b, out = data[i+1 : i+4]
        return a, b, out, lambda x, y: x * y
