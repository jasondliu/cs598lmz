import threading
threading.stack_size(2**27)
import sys
sys.setrecursionlimit(10**7)
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

class Graph():
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def BFS(self, s):
        visited = [False] * (self.V)
        q = []
        visited[s] = True
        q.append(s)

        while q:
            s = q.pop(0)
            print(s, end=' ')

            for i in self.graph[s]:
                if not visited[i]:
                    q.append(i)
                    visited[i] = True


g = Graph(4)
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2
