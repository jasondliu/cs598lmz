import threading
threading.stack_size(2**27)
import sys
sys.setrecursionlimit(10**7)
sys.stdin = open("input.txt", "r")
sys.stdout = open("output.txt", "w")
from math import *
from queue import PriorityQueue
from collections import deque,defaultdict
from functools import lru_cache
from heapq import heappush,heappop
from bisect import bisect_left,bisect
from time import time
inf = float("inf")
mod = 1000000007
eps = 1e-7

def main():
    n = int(input())
    a = list(map(int,input().split()))
    ans = []
    for i in range(n):
        if i == 0:
            ans.append(a[i])
        elif i == 1:
            ans.append(a[i])
        elif i == 2:
            ans.append(a[i])
        elif i == 3:
            ans.append(a[i])
        elif i == 4:

