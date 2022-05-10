import threading
threading.stack_size(2**27)
import sys
sys.setrecursionlimit(10**7)
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

class Graph:

    def __init__(self,vertices):
        self.V= vertices
        self.graph = defaultdict(list)


    def addEdge(self,u,v):
        self.graph[u].append(v)

    def DFSUtil(self,v,visited):
        visited[v]= True
        print(v,end=" ")

        for i in self.graph[v]:
            if visited[i]==False:
                self.DFSUtil(i,visited)

    def fillOrder(self,v,visited, stack):
        visited[v]= True

        for i in self.graph[v]:
            if visited[i]==False:
                self.fillOrder(i, visited, stack)

        stack = stack.append(v)

    def getTranspose(self
