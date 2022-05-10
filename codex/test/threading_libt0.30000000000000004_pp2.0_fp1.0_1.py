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
    a = list(map(int, input().split()))
    dp = [0] * n
    dp[0] = a[0]
    dp[1] = a[1]
    dp[2] = a[2]
    for i in range(3, n):
        dp[i] = max(dp[i-1], dp[i-2], dp[i-3]) + a[i]
