import threading
threading.stack_size(2**27)
import sys
sys.setrecursionlimit(10**7)
sys.stdin = open('inpy.txt', 'r')
sys.stdout = open('outpy.txt', 'w')
from math import *
from collections import *
from queue import PriorityQueue
from heapq import heappush, heappop

MOD = 10 ** 9 + 7

def MI(): return map(int, input().split())
def MI0(): return map(lambda s: int(s) - 1, input().split())
def LI(): return list(map(int, input().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]


def check(arr, n, m, row, col, visited):
    if row < 0 or col < 0 or row >= n or col >= m or visited[row][col] or arr[row][col] == '#':
        return False
    return True


def bfs(arr, n, m, row, col, visited):
    q = deque()
   
