import threading
threading.stack_size(2**27)
import sys
sys.setrecursionlimit(10**7)
sys.stdin = open('inpy.txt', 'r')
sys.stdout = open('outpy.txt', 'w')
from math import *
from collections import deque, Counter
from collections import defaultdict as dd
from itertools import combinations as comb
from itertools import permutations as perm
from itertools import product as prod
from functools import lru_cache as lc
import heapq as hq
from bisect import bisect_left, bisect_right
from copy import deepcopy as copy
import operator as op
from fractions import Fraction
from string import ascii_lowercase, ascii_uppercase, digits

mod = 10 ** 9 + 7
inf = float('inf')
pi = acos(-1)
e = exp(1)

DEBUG = 1


def debug(*args, **kwargs):
    """Print debugging statements"""
    print(*args, **kwargs)


if DEBUG:
    def debug_print(*args
