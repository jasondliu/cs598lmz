import threading
threading.stack_size(2**27)
import sys
sys.setrecursionlimit(10**7)
sys.stdin = open('inpy.txt', 'r')
sys.stdout = open('outpy.txt', 'w')
from math import *
from collections import *
from collections import deque, defaultdict, Counter
from heapq import heappush, heappop
from itertools import permutations, accumulate, combinations, product
from operator import itemgetter
from bisect import bisect_left, bisect_right, bisect
from functools import reduce
from string import ascii_lowercase, ascii_uppercase, digits

def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int, input().split())
def S_MAP(): return map(str, input().split())
def LIST(): return list(map(int, input().split()))
def S_LIST(): return list(map(str, input().split()))

sys.setrecursionlimit(10 ** 9)

