import threading
threading.stack_size(2**27)
import sys
sys.setrecursionlimit(10**7)
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
from math import *
from collections import *
from queue import PriorityQueue
from bisect import bisect_left, bisect_right
from itertools import *
from copy import deepcopy

mod = 1000000007
inf = int(1e18)

n = int(input())
a = list(map(int, input().split()))

def solve():
    dp = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        dp[i][i] = a[i]
    for i in range(n):
        for j in range(i + 1, n):
            dp[i][j] = dp[i][j - 1] ^ a[j]
    ans = 0
