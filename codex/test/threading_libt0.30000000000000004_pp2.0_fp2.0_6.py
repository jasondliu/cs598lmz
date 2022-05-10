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
from itertools import permutations, combinations
from copy import deepcopy

mod = 1000000007
inf = 10**9

n, m = map(int, input().split())

if n == 1 and m == 0:
    print(1)
    exit()

if n == 1 or m == 0:
    print(0)
    exit()

dp = [[0 for i in range(m + 1)] for j in range(n + 1)]

dp[1][0] = 1

