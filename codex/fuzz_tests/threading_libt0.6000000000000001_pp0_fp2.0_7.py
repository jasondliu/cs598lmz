import threading
threading.stack_size(2**27)
import sys
sys.setrecursionlimit(10**7)
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')


from itertools import product

class Graph:
    def __init__(self, n):
        self.n = n
        self.graph = [[] for _ in range(n)]

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def dfs(self, node, parent):
        for child in self.graph[node]:
            if parent != child:
                self.dfs(child, node)

    def get_nodes(self):
        return self.n


def bfs(graph, start, end):
    queue = deque()
    queue.append([start])
    visited = set()
    visited.add(start)
    while queue:
        path = queue.popleft()
        node = path
