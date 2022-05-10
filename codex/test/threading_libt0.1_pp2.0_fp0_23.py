import threading
threading.stack_size(2**27)
import sys
sys.setrecursionlimit(10**7)
sys.stdin = open('inpy.txt', 'r')
sys.stdout = open('outpy.txt', 'w')
from math import *
from collections import *
from queue import PriorityQueue
from heapq import heapify, heappop, heappush

def main():
    n, m = map(int, input().split())
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]
    a.sort()
    b.sort()
    i = 0
    j = 0
    ans = 0
    while i < n and j < m:
        if a[i] <= b[j]:
            ans += 1
            i += 1
            j += 1
        else:
            j += 1
    print(ans)

