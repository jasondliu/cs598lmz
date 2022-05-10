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
 
blue, red, green = '0123456789ABCDEF'
MOD = 10 ** 9 + 7
# template {{{
# n = int(input())
# a = list(map(int, input().split()))
# n, m = map(int, input().split())
# a = [[int(i) for i in input().split()] for _ in range(n)]
# p = [int(i) for i in input().split()]
# }}}


def solve():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ans = 0
    for i in range(n):
        ans += abs(a
