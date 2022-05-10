import threading
threading.stack_size(2**27)

import sys
sys.setrecursionlimit(10**7)

sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

from collections import defaultdict
from collections import deque
import math
import heapq

class Graph:
    def __init__(self, n):
        self.n = n
        self.edges = defaultdict(list)
        self.parent = [i for i in range(n)]
        self.size = [1 for i in range(n)]

    def add_edge(self, x, y):
        self.edges[x].append(y)
        self.edges[y].append(x)

    def find(self, x):
        if self.parent[x] == x:
            return x
        return self.find(self.parent[x])

    def union(self, x, y):
        px = self.find(x)
        py = self.find(y)
