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

MOD = 10 ** 9 + 7

# graph
n, m = [int(x) for x in input().split()]
adj = [[] for i in range(n)]
for i in range(m):
    a, b = [int(x) for x in input().split()]
    adj[a - 1].append(b - 1)
    adj[b - 1].append(a - 1)

# dfs
visited = [False] * n
def dfs(v):
    visited[v] = True
    for i in adj[v]:
        if not visited[i]:
            dfs(i)

# bfs
visited = [False] * n
