import threading
threading.stack_size(2**27)
import sys
sys.setrecursionlimit(10**7)
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
from math import *
from collections import deque
from queue import PriorityQueue
from bisect import bisect_left, bisect_right

mod = 10 ** 9 + 7
inf = float('inf')

n, m, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))


def solve():
    t = 0
    i = 0
    j = 0
    ans = 0
    while i < n and j < m:
        if a[i] <= b[j] + k and b[j] <= a[i] + k:
            t += 1
            i += 1
            j += 1
            ans = max(ans, t)
        elif a[i] < b[j] + k:
            i += 1

