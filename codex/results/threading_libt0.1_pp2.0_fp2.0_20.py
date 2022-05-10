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

mod = 10 ** 9 + 7
inf = float('inf')
ninf = -float('inf')

#---------------------------_/\_Main Program Start Here_/\_------------------
def main():
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    ans = 0
    for i in range(n):
        ans += abs(arr[i] - (i + 1))
    print(ans)


t = int(input())
for i in range(t):
    main()
