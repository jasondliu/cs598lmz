import threading
threading.stack_size(2**27)
import sys
sys.setrecursionlimit(10**7)
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
from math import *
from collections import defaultdict
from collections import deque
from collections import Counter
from heapq import heappush, heappop

class Graph:
    def __init__(self, n):
        self.n = n
        self.edges = defaultdict(list)

    def addEdge(self, u, v):
        self.edges[u].append(v)
        self.edges[v].append(u)

    def bfs(self, s):
        visited = [False] * self.n
        visited[s] = True
        q = deque()
        q.append(s)
        while q:
            u = q.popleft()
