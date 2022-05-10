import threading
threading.stack_size(2**27)
import sys
sys.setrecursionlimit(10**7)
sys.stdin = open('inpy.txt', 'r')
sys.stdout = open('outpy.txt', 'w')
from math import *
from collections import *
from queue import PriorityQueue
from bisect import bisect_left, bisect_right
from itertools import *
from copy import deepcopy
import random
import time
inf = 10**9
mod = 10**9 + 7

def in_grid(x, y):
    if x >= 0 and x < n and y >= 0 and y < m:
        return True
    else:
        return False


def bfs(x, y):
    q = deque([[x, y]])
    vis[x][y] = True
    while q:
        i, j = q.popleft()
        for k in range(4):
            x = i + dx[k]
            y = j + dy[k]
