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
 
blue, red, green = '01#'
 
def merge(clr):
    if clr == '0':
        return 0
    if clr == '1':
        return 1
    return 2
 
def solve(n, m, grid):
    dp = [[[0] * 3 for _ in range(m)] for _ in range(n)]
    dp[0][0][merge(grid[0][0])] = 1
    for i in range(n):
        for j in range(m):
            if i == 0 and j == 0:
                continue
            if grid[i][j] == '#':
                dp[i][j][0] = d
