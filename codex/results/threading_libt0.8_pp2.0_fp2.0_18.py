import threading
threading.stack_size(2147480000)

import sys, time

sys.setrecursionlimit(800000)

class Graph:
    def __init__(self):
        self.edges = [[] for i in range(100000)]
        self.low = [[] for i in range(100000)]
        self.pre = [[] for i in range(100000)]
        self.bridge = [[] for i in range(100000)]
        self.ans = [0 for i in range(100000)]
        self.vis = [0 for i in range(100000)]
        self.cnt = 0
        self.cnt2 = 0
        self.n, self.m = 0, 0

    def add_edge(self, b, e):
        self.edges[b].append(e)
        self.edges[e].append(b)

    def dfs(self, node, par):
        self.vis[node] = 1
        self.pre[node] = par
        self.low[node] = self.cnt
       
