import threading
threading.stack_size(2**27)
import sys
sys.setrecursionlimit(10**7)
sys.stdin = open('inpy.txt', 'r')
sys.stdout = open('outpy.txt', 'w')
from math import *
from collections import deque, Counter
from collections import defaultdict
from heapq import heappush, heappop

gi = lambda: int(input())
gis = lambda: list(map(int, input().split()))
gs = lambda: input()
skiplast = lambda x: range(len(x)-1)
is_even = lambda x: x%2 == 0
half = lambda x: x//2
####################################################################

# def dfs(arr, s, d, visited, h):
#     visited[s] = 1
#     h.append(s)
#     if s == d:
#         return True
#     for i in range(len(arr[s])):
#         if (arr[s][i] == 1) and not visited[i]:
#             a = dfs(arr
