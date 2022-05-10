import threading
threading.stack_size(2**27)
import sys
sys.setrecursionlimit(10**7)
sys.stdin = open('inpy.txt', 'r')
sys.stdout = open('outpy.txt', 'w')
from math import *
from collections import *
from queue import PriorityQueue
from heapq import heappush, heappop

# python -m cProfile -s time ha.py
# python3 -m cProfile -s time ha.py

mod = 10 ** 9 + 7

#---------------------------------------------

def inp(): return int(input())
def inlt(): return list(map(int, input().split()))
def insr(): return input()
def invr(): return map(int, input().split())

#---------------------------------------------

def solve(n):
    ans = 0
    for i in range(1, int(sqrt(n)) + 1):
        if n % i == 0:
            ans += i
            if i != 1 and i != n // i:
                ans += n // i
    return ans

