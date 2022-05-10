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

def read():
    return sys.stdin.readline().strip()

def write(s):
    sys.stdout.write(str(s))

def main():
    n = int(read())
    a = list(map(int, read().split()))
    b = list(map(int, read().split()))
    c = list(map(int, read().split()))
    a.sort()
    b.sort()
    c.sort()
    ans = 0
