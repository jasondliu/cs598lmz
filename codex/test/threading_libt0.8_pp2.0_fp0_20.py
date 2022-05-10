import threading
threading.stack_size(2**27)
import sys
sys.setrecursionlimit(10**7)
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

#Code starts here
class Graph():
    def __init__(self,nodes):
        self.nodes=nodes
        self.adj_list={}

    def add_edge(self,u,v):
        if u not in self.adj_list:
            self.adj_list[u]=[v]
        else:
            self.adj_list[u].append(v)

        if v not in self.adj_list:
            self.adj_list[v]=[u]
        else:
            self.adj_list[v].append(u)

def check_cycle(graph,node,visited,rec_stack):
    visited[node]=True
    rec_stack[node]=True
