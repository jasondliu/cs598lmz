import threading
threading.stack_size(2**27)
import sys
sys.setrecursionlimit(10**7)
sys.stdin = open('inpy.txt', 'r')
sys.stdout = open('outpy.txt', 'w')
from math import *
from collections import *
from queue import PriorityQueue
from heapq import heapify, heappop, heappush
 
blue, red, white = '0', '1', '.'
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
 
def inside(y, x, n, m):
    return 0 <= y < n and 0 <= x < m
 
def bfs(y, x, c):
    q = deque()
    q.append((y, x))
    visited[y][x] = 1
    while q:
        y, x = q.popleft()
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
