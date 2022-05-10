import threading
threading.stack_size(2**27)
import sys
sys.setrecursionlimit(10**7)
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

class Graph:

    def __init__(self, size):
        self.size = size
        self.arr = [[] for i in range(size)]

    def addEdge(self, v1, v2):
        self.arr[v1].append(v2)
        self.arr[v2].append(v1)

    def __dfs(self, v, visited):
        visited[v] = True
        for i in self.arr[v]:
            if not visited[i]:
                self.__dfs(i, visited)

    def countComponents(self):
        visited = [False for i in range(self.size)]
        count = 0
        for i in range(self.size):
            if not visited[i]:
                self.__dfs(i, visited)
                count += 1
        return count
