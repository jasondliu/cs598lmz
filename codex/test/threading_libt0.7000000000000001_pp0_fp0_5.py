import threading
threading.stack_size(2**27)
import sys
sys.setrecursionlimit(10**7)
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
from collections import Counter
from math import gcd
from fractions import Fraction
from decimal import Decimal
from bisect import bisect, bisect_left, bisect_right
from itertools import permutations
from heapq import heapify, heappop, heappush
from queue import PriorityQueue
from time import time
def lcm(a, b): return (a * b) // gcd(a, b)
cinp = lambda: [int(x) for x in input().split()]
cinp_list = lambda: list(map(int, input().split()))
MOD = 10**9+7

#---------------------------------------------

def solve(a, b, k):
    if k >= a and k >= b:
        return 1
    if k < a and k < b:
        return 0
