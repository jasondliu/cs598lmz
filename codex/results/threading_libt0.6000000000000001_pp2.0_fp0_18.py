import threading
threading.stack_size(2**27)
import sys
sys.setrecursionlimit(10**7)
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
from math import *
from fractions import *
from collections import *
from queue import PriorityQueue
from heapq import heapify, heappop, heappush
 
 
def inp(): return int(input())
def inp_list(): return list(map(int, input().split()))
 
 
def bfs(graph, start):
    visited, queue = set(), [start]
    while queue:
        vertex = queue.pop(0)
        for neighbour in graph[vertex]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)
    return visited
 
 
def main():
    n, m = inp_list()
    graph = defaultdict(list)
    for i in range(m):
        u, v = inp_list()
        graph
