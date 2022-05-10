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
n, m = map(int, input().split())
g = [[] for i in range(n + 1)]
for i in range(m):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)


def bfs(src):
    vis = [False] * (n + 1)
    vis[src] = True
    q = deque()
    q.append(src)
    while q:
        cur = q.popleft()
        for i in g[cur]:
            if not vis[i]:
                vis[i] = True
                q.append
