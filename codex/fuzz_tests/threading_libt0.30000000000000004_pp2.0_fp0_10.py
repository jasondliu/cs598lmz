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
inf = 10**18
mod = 10**9 + 7

def pw(x, y):
    return x**y

def inv(x):
    return pow(x, mod - 2, mod)

def binpow(x, y):
    res = 1
    while y > 0:
        if y & 1:
            res = res * x % mod
        x = x * x % mod
        y >>= 1
    return res

def binpow(x, y):
    res = 1
    while y > 0:
        if y & 1:
            res = res * x % mod
        x =
