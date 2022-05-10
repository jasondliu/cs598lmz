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
from itertools import accumulate,permutations,combinations,product,combinations_with_replacement
from operator import itemgetter
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from datetime import date

def floor(x): return int(x) if x - int(x) < 0.5 else int(x) + 1
def ceil(x): return int(x) if x - int(x) > 0.5 else int(x) + 1
def round(x): return floor(x + 0.5)
def fermat(x, y, MOD): return x * pow(y, MOD-2, MOD) % MOD
def lcm(x
