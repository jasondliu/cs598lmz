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
from itertools import permutations, combinations
from copy import deepcopy
import string
import time
inf = float('inf')
mod = 10**9 + 7

def inp(): return int(input())
def inp_list(): return list(map(int, input().split()))

# --------------------------------------------------------------------------------------

def solve(n, m, k, a, b, c):
    if k == 0:
        return 0
    if k == 1:
        return min(a[0], b[0], c[0])
