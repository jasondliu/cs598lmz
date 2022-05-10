import threading
threading.stack_size(2**27)
import sys
sys.setrecursionlimit(10**7)
sys.stdin = open('inpy.txt', 'r')
sys.stdout = open('outpy.txt', 'w')
from math import *
from collections import *
from queue import PriorityQueue
from bisect import bisect_left, bisect_right
from itertools import permutations, combinations, product, accumulate
from operator import itemgetter, xor, add
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from datetime import datetime

def shift_right(l):
    return [l[-1]] + l[:-1]

def shift_left(l):
    return l[1:] + [l[0]]

def binpow(a, n):
    res = 1
    while n:
        res *= a
        n >>= 1
    return res

def gcd(a, b):
    while b > 0:
        a, b = b, a %
