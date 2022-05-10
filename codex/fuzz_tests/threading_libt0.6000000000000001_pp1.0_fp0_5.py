import threading
threading.stack_size(2**27)
import sys
sys.setrecursionlimit(10**7)
sys.stdin = open('inpy.txt', 'r')
sys.stdout = open('outpy.txt', 'w')
from math import *
from collections import deque, Counter
from itertools import combinations, permutations

def dijkstra(n, s, adj):
    dist = [inf] * n
    dist[s] = 0

    q = set([i for i in range(n)])
    while q:
        u = min(q, key=lambda x: dist[x])
        q.remove(u)

        for v,w in adj[u]:
            dist[v] = min(dist[v], dist[u] + w)

    return dist

def dijkstra2(n, s, adj):
    dist = [inf] * n
    dist[s] = 0

    q = set([i for i in range(n)])
    while q:
        u = min(q, key=lambda x:
