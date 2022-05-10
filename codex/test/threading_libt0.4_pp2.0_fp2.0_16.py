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


    def DFSUtil(self,v,visited,parent):

        # Mark the current node as visited
        visited[v]= True

        #Recur for all the vertices adjacent to this vertex
        for i in self.graph[v]:
            if  visited[i]==False :
                if(self.DFSUtil(i,visited,v)):
                    return True

            elif  parent!=i:
                return True

        return False


