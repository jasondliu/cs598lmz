import threading
threading.stack_size(2**27)
import sys
sys.setrecursionlimit(10**7)
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

class Graph:

    def __init__(self,size):
        self.size=size
        self.arr=[[0 for i in range(size)] for j in range(size)]

    def add_edge(self,v1,v2):
        self.arr[v1][v2]=1
        self.arr[v2][v1]=1

    def remove_edge(self,v1,v2):
        if self.contains_edge(v1,v2):
            self.arr[v1][v2]=0
            self.arr[v2][v1]=0
            return True
        else:
            return False

    def contains_edge(self,v1,v2):
        return True if self.arr[v1][v2]>0 else False

    def __str__(self):
        return
