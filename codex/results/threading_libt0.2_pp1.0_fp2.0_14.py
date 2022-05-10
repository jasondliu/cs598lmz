import threading
threading.stack_size(2**27)
import sys
sys.setrecursionlimit(10**7)
sys.stdin = open('inpy.txt', 'r')
sys.stdout = open('outpy.txt', 'w')
from math import *
from collections import *
from queue import PriorityQueue
from bisect import bisect_left, bisect_right
from itertools import permutations, combinations, product, accumulate, combinations_with_replacement
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from functools import reduce
def inin(): return int(input())
def stin(): return [int(x) for x in input().split()]
def spin(): return [int(x) for x in input()]
def lin(): return [i for i in input()]
def matrix(n): return [list(map(int, input().split())) for i in range(n)]

##############################################################

test = 1
# test = inin()
for _ in range(test):
    n =
