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

    def add_undirected_edge(self, src, dest):
        self.arr[src].append(dest)
        self.arr[dest].append(src)

    def add_directed_edge(self, src, dest):
        self.arr[src].append(dest)

    def print_graph(self):
        for i in range(self.size):
            print(i, end = "->")
            for j in self.arr[i]:
                print(j, end = ", ")
            print()

def createLevelLinkedList(root):
    result = []
    current = []
    if root is not None:
        current.append(root)

