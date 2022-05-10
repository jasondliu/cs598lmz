import threading
threading.stack_size(2**27)
import sys
sys.setrecursionlimit(10**7)
sys.stdin = open('inpy.txt', 'r')
sys.stdout = open('outpy.txt', 'w')
from math import *
from collections import defaultdict
from collections import deque
from queue import PriorityQueue
from bisect import bisect_left, bisect_right
from itertools import permutations, combinations
from itertools import accumulate, product, combinations_with_replacement
from functools import reduce
def inin(): return int(input())
def stin(): return [int(e) for e in input().split()]
def spin(): return [int(e) for e in input().split()]
def lin(): return [e for e in input().split()]
def matrix(n): return [list(map(int, input().split())) for _ in range(n)]
def List(n, ini=None): return [ini for _ in range(n)]
