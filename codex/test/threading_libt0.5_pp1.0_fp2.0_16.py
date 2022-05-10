import threading
threading.stack_size(2**27)
import sys
sys.setrecursionlimit(10**7)
sys.stdin = open('inpy.txt', 'r')
sys.stdout = open('outpy.txt', 'w')
from math import *
from collections import *
from queue import PriorityQueue
from heapq import heapify, heappop, heappush

mod = 10 ** 9 + 7
inf = 1e18
ninf = -1e18

#---------------------------_/\_Main Program Start Here_/\_------------------
def Main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.sort()
    b.sort()
    ans = 0
    for i in range(m):
        if a[0] < b[i]:
            ans += 1
            a.pop(0)
    print(ans)


if __name__ == '__main__':
    Main()
