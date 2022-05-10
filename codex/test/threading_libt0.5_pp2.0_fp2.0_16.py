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

MOD = 1000000007

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    ans = 0
    for i in range(n):
        cur = i
        for j in range(i + 1, n):
            if a[j] < a[cur]:
                cur = j
        if cur != i:
            ans += 1
            a[i], a[cur] = a[cur], a[i]

    print(ans)
