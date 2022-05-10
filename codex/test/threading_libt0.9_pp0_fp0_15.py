import threading
threading.stack_size(2**27)
import sys
sys.setrecursionlimit(10**7)
sys.stdin = open('inXYZ.txt', 'r')
sys.stdout = open('outXYZ.txt', 'w')
from collections import defaultdict, deque, Counter
from time import time
t = time()
from math import gcd, log, floor, sqrt, factorial
from heapq import heappop, heappush, heapify
inf = 10**9 + 7
INF = float('inf')
from functools import reduce
def lcm(a, b): return a * b // gcd(a, b)
sys.setrecursionlimit(1000000)
##################################  debug  #########################################
def no(): return print(-1)
def yes(): print('YES')
def No(): print('NO')
def YES(): print('YES')
def NO(): print('NO')
def lcm_list(numbers):
    return reduce(lcm, numbers, 1)
