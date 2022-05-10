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

def main():
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    ans = [0 for i in range(n)]
    for i in range(n):
        if i % 2 == 0:
            ans[i//2] = arr[i]
        else:
            ans[n//2 + i//2] = arr[i]
    print(*ans)

main()
