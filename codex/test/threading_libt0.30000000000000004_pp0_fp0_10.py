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

mod = 10 ** 9 + 7
inf = 10 ** 20

nax = 2 * 10 ** 5 + 5

n, m = map(int, input().split())

# dp[i][j] = max number of elements in a subset of size j from first i elements
dp = [[0 for i in range(m + 1)] for j in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, m + 1):
        if j == 1:
            dp[i][j] = i
