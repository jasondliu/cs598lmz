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
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]
    c = [int(x) for x in input().split()]
    ans = 0
    for i in range(n):
        ans += b[a[i]-1]
        if i > 0 and a[i] == a[i-1] + 1:
            ans += c[a[i-1]-1]
    print(ans)

main()
