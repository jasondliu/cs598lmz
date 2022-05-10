import threading
threading.stack_size(2**27)
import sys
sys.setrecursionlimit(10**7)
sys.stdin = open('inpy.txt', 'r')
sys.stdout = open('outpy.txt', 'w')
from math import *
from collections import deque, Counter
from collections import defaultdict as dd
from itertools import permutations, combinations, accumulate
from operator import itemgetter as ig
from functools import lru_cache as lc
import heapq
from copy import deepcopy
import itertools
ints = lambda x: int(x.strip())
floats = lambda x: list(map(float, x.strip().split()))
strings = lambda x: list(x.strip().split())
def q1(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    elif n == 3:
        return 2
    else:
        return 3 + q1(n-3)
def q2(n):
    if n == 1:
        return 0
    elif n ==
