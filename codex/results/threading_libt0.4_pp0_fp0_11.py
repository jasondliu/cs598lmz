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

mod = 1000000007

#### FLOYD WARSHALL ####

def solve(n, m, edges, s, t):
    dist = [[0 if i == j else float('inf') for i in range(n)] for j in range(n)]
    for u, v, w in edges:
        dist[u][v] = w
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    return dist[s][t]


n, m = map(int, input().split())
edges = []
for i
