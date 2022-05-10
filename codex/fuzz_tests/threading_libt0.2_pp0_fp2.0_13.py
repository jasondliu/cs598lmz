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
def write(s): sys.stdout.write(s)
def writeln(s): sys.stdout.write(s + '\n')
def read_array(H, W, foo=int): return [foo(x) for x in read().split() for _ in range(W)]
def read_2d_array(H, W, foo=int): return [read_array(H, W, foo) for _ in range(H)]
def array(length, foo=int):
