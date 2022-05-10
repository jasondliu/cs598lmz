import threading
threading.stack_size(2**27)
import sys
sys.setrecursionlimit(10**7)
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
from math import inf, sqrt, log
from heapq import heappop, heappush, heapify
from collections import Counter, defaultdict, deque
from itertools import accumulate, permutations, combinations, product, cycle
from bisect import bisect_left, bisect_right
from copy import deepcopy
from fractions import Fraction
from string import ascii_lowercase, ascii_uppercase, digits

mod = 1000000007
inf = float('inf')
ninf = -float('inf')
 
#-----------------------START OF CODE---------------
# t = int(input())
# while t:
#     n = int(input())
#     s = input().strip()
#     d = {}
#     for c in s:
#         d[c] = d.get(c, 0) + 1
#     l = list
