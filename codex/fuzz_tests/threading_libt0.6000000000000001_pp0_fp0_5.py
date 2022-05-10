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

    def topologicalSort(self,v,visited,stack):

        visited[v]= True

        for i in self.graph[v]:
            if visited[i]==False:
                self.topologicalSort(i,visited,stack)

        stack.append(v)

    def topologicalSortUtil(self):
        visited =[False]*self.V
        stack =[]

        for i in range(self.V):
            if visited[i]==False:
                self.topologicalSort(i,visited,stack)

        print(stack[::-1])

