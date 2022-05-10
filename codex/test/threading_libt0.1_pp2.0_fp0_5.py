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

def pw(a, n, m):
    res = 1
    while n:
        if n & 1:
            res = (res * a) % m
        a = (a * a) % m
        n >>= 1
    return res

def inv(a, m):
    return pw(a, m - 2, m)

def solve():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
