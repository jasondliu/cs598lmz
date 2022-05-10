import threading
threading.stack_size(2**27)
import sys
sys.setrecursionlimit(10**9)
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
from collections import deque

class Vertex:
    def __init__(self, id):
        self.id = id
        self.connections = []

class Graph:
    def __init__(self, arrs):
        self.vertList = {}
        self.numVertices = 0
        self.predecessors = {}
        self.arrs = arrs
        self.change_number = 0
        self.time = 0

        # self.dfs()
        self.BFS()

    def BFS(self):
        v = Vertex(0)
        self.addVertex(v)
        self.vertList[0].connections = [-1,0]*len(self.arrs)
        self.predecessors[0] = 0

        for i in range(1,n):
            v = Ver
