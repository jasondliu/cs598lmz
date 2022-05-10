import threading
threading.stack_size(2**27)
import sys
sys.setrecursionlimit(10**7)
sys.stdin = open('inpy.txt', 'r')
sys.stdout = open('outpy.txt', 'w')
from math import *
from collections import deque, Counter
from collections import defaultdict as dd
from heapq import heappush, heappop, heapify
from bisect import bisect_left, bisect_right
from itertools import permutations, combinations, accumulate
from operator import itemgetter, mul
from copy import deepcopy
from fractions import gcd
from random import randint


def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.sort()
    b.sort(reverse=True)

    for i in range(m):
        if a[i] < b[i]:
            a[i] = b[i]
        else:
            break
    print(sum(
