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
 
#----------------------------------------#
def main():
    n = int(input())
    a = list(map(int, input().split()))
    a = [0] + a
    dp = [0] * (n+1)
    dp[0] = 1
    for i in range(1, n+1):
        for j in range(i):
            if a[j] < a[i]:
                dp[i] += dp[j]
    print(sum(dp) % mod)


    return

#----------------------------------------#
