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

def pw(a, n, mod=mod):
    if n == 0:
        return 1
    if n % 2:
        return (a * pw(a, n - 1, mod)) % mod
    b = pw(a, n // 2, mod)
    return (b * b) % mod

def inv(a, mod=mod):
    return pw(a, mod - 2, mod)

def solve():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
   
