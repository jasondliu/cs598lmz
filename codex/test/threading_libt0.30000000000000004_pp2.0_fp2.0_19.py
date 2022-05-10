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
def solve():
    n, m = map(int, input().split())
    grid = [list(input()) for i in range(n)]
    ans = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == white:
                ans += 1
                dfs(grid, i, j)
    print(ans)
 
def dfs(grid, i, j):
    if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != white:
        return
    grid[i][j]
