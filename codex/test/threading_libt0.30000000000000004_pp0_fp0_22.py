import threading
threading.stack_size(2**27)
import sys
sys.setrecursionlimit(10**7)
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
from math import *
from collections import defaultdict, deque
from heapq import heappush, heappop, heapify

class Graph:
    def __init__(self, n):
        self.n = n
        self.edges = defaultdict(list)

    def addEdge(self, u, v, w):
        self.edges[u].append((v, w))
        self.edges[v].append((u, w))

    def dijkstra(self, s):
        dist = [inf] * self.n
        dist[s] = 0
        pq = [(0, s)]
        while pq:
            d, u = heappop(pq)
            if dist[u] < d: continue
