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

mod = 10 ** 9 + 7
inf = float('inf')
ninf = -float('inf')

#---------------------------_/\_Main Program Start Here_/\_------------------
t = int(input())
for Case in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        for j in range(i + 1, n):
            ans += arr[i] * arr[j]
    print(ans)
