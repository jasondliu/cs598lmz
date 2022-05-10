import threading
threading.stack_size(2**27)
import sys
sys.setrecursionlimit(10**7)
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
from math import *
from collections import *
from queue import PriorityQueue
from bisect import bisect_left, bisect_right
from itertools import *
from copy import deepcopy
from functools import reduce
from string import ascii_lowercase, ascii_uppercase, digits

def read(): return sys.stdin.readline().strip()
def write(s): sys.stdout.write(str(s))
def writeln(s): sys.stdout.write(str(s) + '\n')
def read_array(t, n): return [t(x) for x in sys.stdin.readline().strip().split()[:n]]
def write_array(a): sys.stdout.write(' '.join([str(x) for x in a]))

n = int(read())
a = read
