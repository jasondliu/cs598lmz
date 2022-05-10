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

def pw(a, n):
    if n == 0:
        return 1
    if n % 2 == 1:
        return pw(a, n - 1) * a % mod
    return pw(a * a % mod, n // 2)

def inv(a):
    return pw(a, mod - 2)

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    if n == 1:
        print(a[0])
        return
    if n == 2:
        print
