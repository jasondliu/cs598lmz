import threading
threading.stack_size(2**27)
import sys
sys.setrecursionlimit(10**7)
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

class Graph:

    def __init__(self, size):
        self.size = size
        self.arr = [[] for _ in range(size)]

    def add_undirected_edge(self, first, second):
        self.arr[first].append(second)
        self.arr[second].append(first)

    def add_directed_edge(self, first, second):
        self.arr[first].append(second)

    def print_graph(self):
        print(self.arr)

    def bfs(self, start, finish):
        queue = deque()
        queue.append(start)
        visited = [False] * self.size
        visited[start] = True
        while queue:
            v = queue.popleft()
