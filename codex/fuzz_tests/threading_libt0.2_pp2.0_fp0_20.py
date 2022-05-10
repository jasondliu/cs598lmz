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
inf = float('inf')
ninf = -float('inf')
 
#----------------------------------------#
def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    a.sort()
    ans = 0
    for i in range(n):
        ans += abs(a[i] - (i + 1))
    print(ans)
 
 
if __name__ == '__main__':
    main()
