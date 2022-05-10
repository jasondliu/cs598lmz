import threading
threading.stack_size(2**27)
import sys
sys.setrecursionlimit(10**7)
sys.stdin = open('inpy.txt', 'r')
sys.stdout = open('outpy.txt', 'w')
from math import *
from collections import *
from collections import deque, Counter
from operator import itemgetter
from itertools import permutations, combinations, accumulate
from string import ascii_uppercase, ascii_lowercase
from bisect import bisect_left, bisect_right
from fractions import gcd
from heapq import heappush, heappop
from functools import reduce
import time


def main():
    t = int(input())
    while t > 0:
        t -= 1
        n = int(input())
        a = list(map(int, input().split()))
        dp = [[0] * n for i in range(n)]
        dp[0][0] = a[0]
        for i in range(1, n):
            for j in range(i + 1):

