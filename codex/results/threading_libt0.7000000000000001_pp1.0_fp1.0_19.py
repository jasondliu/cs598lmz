import threading
threading.stack_size(2**27)
import sys
sys.setrecursionlimit(10**9)
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
from math import gcd, ceil
from itertools import permutations, combinations, combinations_with_replacement, product
from collections import deque, defaultdict, Counter
from operator import itemgetter
from bisect import bisect_left, bisect, bisect_right
from heapq import heappush, heappop, heapify
from fractions import Fraction
def lcm(a,b): return (a*b) // gcd(a,b)
#-------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------

# https://codeforces.com/problemset/problem/1343/B

def solve(n):
    if n % 4 != 0:
        return 'NO'
    arr = [0] * n
    m = n // 2
    for i in range(1, m + 1):
        arr[i - 1] = i *
