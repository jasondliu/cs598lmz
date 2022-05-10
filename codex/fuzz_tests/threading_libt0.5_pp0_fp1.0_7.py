import threading
threading.stack_size(2**27)
import sys
sys.setrecursionlimit(10**7)
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
from math import *
from queue import PriorityQueue
from collections import *
from itertools import *
from functools import *
from string import ascii_lowercase
from bisect import bisect_left, bisect

gi = lambda: int(input())
gis = lambda: list(map(int, input().split()))
gs = lambda: input()
skiplast = lambda x: range(len(x)-1)
inf = float('inf')

n = gi()

a = gis()

dp = [[0] * n for _ in range(n)]

for i in range(n):
    dp[i][i] = a[i] * n

for l in range(2, n+1):
    for i in range(n):
        j = i + l - 1
        if j >= n
