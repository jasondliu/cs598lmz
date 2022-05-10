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

MOD = 1000000007

# template ends here

n, m = map(int, input().split())
a = list(map(int, input().split()))

if m >= n:
    print(0)
    exit()

a.sort()

ans = a[m] - a[0]
for i in range(1, n - m + 1):
    ans = min(ans, a[i + m - 1] - a[i])

print(ans)
