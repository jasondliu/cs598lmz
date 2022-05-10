import threading
threading.stack_size(2**27)
import sys
import math
sys.setrecursionlimit(10**7)
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

class Graph:

    def __init__(self,vertices):
        self.V= vertices
        self.graph = defaultdict(list)


    def addEdge(self,u,v):
        self.graph[u].append(v)


    def BFS(self,s):

        visited = [False]*(self.V)

        queue=[]

        queue.append(s)
        visited[s] = True

        while queue:

            s = queue.pop(0)
            print (s, end = " ")

            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True


g = Graph(4)
g.addEdge(0, 1)
g.addEdge(0, 2)

