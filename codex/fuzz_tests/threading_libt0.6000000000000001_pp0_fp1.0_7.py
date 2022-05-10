import threading
threading.stack_size(2**27)
import sys
sys.setrecursionlimit(10**7)
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

from collections import defaultdict, deque
import heapq

class Graph:
    def __init__(self,n):
        self.n = n
        self.edges = defaultdict(list)

    def add_edges(self,u,v,w):
        self.edges[u].append([v,w])

    def dijkstra(self,src):
        dist = [float("inf") for _ in range(self.n)]
        dist[src] = 0
        pq = []
        heapq.heappush(pq, [0, src])

        while pq:
            w, u = heapq.heappop(pq)
            if dist[u] < w:
                continue

            for v, weight in self.edges[u]:
                if dist[v] > dist[u
