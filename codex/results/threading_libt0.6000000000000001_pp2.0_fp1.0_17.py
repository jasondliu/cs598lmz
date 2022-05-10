import threading
threading.stack_size(2**27)
import sys
sys.setrecursionlimit(10**7)
sys.stdin = open('inpy.txt', 'r')
sys.stdout = open('outpy.txt', 'w')
from collections import Counter
from collections import defaultdict
from collections import deque
import math
from heapq import heappush, heappop

import random
from math import factorial
inf = 10 ** 18
mod = 10 ** 9 + 7

def L(): return list(map(int, input().split()))
def LL(): return [list(map(int, l.split())) for l in input()]
def PL(): return [list(map(int, l.split())) for l in input().split()]
def SL(): return list(input())
def VI(n, init=0): return [VI(n, init) for _ in range(n)]
def VVI(n, m, init=0): return [[VI(m, init) for _ in range(n)] for _ in range(n)]

def fact(n): return fact
