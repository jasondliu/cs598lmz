import threading
threading.stack_size(2**27)
import sys
sys.setrecursionlimit(10**7)
sys.stdin = open('inpy.txt', 'r')
sys.stdout = open('outpy.txt', 'w')
from math import *
from collections import *
from collections import deque, Counter; from heapq import heappush, heappop
from itertools import *
from functools import *
from bisect import bisect_left, bisect_right
from decimal import Decimal
inf = float('inf')
mod = 1000000007
#=========================================================================================
#=========================================================================================
def main():
    n = i()
    a = [i() for i in range(n)]
    b = [i() for i in range(n)]
    a.sort()
    b.sort()
    c = 0
    for i in range(n):
        c += a[i] * b[n-i-1]
    print(c)

def i(): return int(input())
def s(): return input()
def ii(): return int
