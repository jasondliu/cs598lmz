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
from itertools import permutations, combinations, product, accumulate, combinations_with_replacement
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from functools import reduce
def inin(): return int(input())
def stst(): return input().split()
def get_min(in_): return min(in_)  # optional
def get_max(in_): return max(in_)  # optional
def display(a, n, m):
    for i in range(n):
        for j in range(m):
            print(a[i][j], end=' ')
        print()
def sieve(n):
    prime = [True
