import threading
threading.stack_size(2**27)
import sys
sys.setrecursionlimit(10**9)
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
from math import sqrt, log
from heapq import heappop, heappush, heappushpop
from collections import Counter, defaultdict, deque
from itertools import accumulate, permutations, combinations, product, combinations_with_replacement
from bisect import bisect_left, bisect_right, bisect
from copy import deepcopy
from operator import itemgetter, mul
from functools import reduce, partial
from fractions import Fraction
from string import ascii_lowercase, ascii_uppercase, digits
from datetime import date
def read(): return input().strip()
def iread(): return int(input().strip())
def vi(s, sep=' '): return [i for i in s.split(sep) if i]
def mts(m): return [vi(x) for x in m]
