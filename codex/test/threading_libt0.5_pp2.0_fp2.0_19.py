import threading
threading.stack_size(2**27)
import sys
sys.setrecursionlimit(10**7)
sys.stdin = open('inpy.txt', 'r')
sys.stdout = open('outpy.txt', 'w')
from math import *
from collections import deque, Counter
from collections import defaultdict as dd
from itertools import accumulate, permutations, combinations, product
from operator import itemgetter as ig
from functools import lru_cache as lc
import heapq
from queue import Queue
import string

def printGrid(grid):
    for i in range(h):
        print(*grid[i])

def printAns(ans):
    print(*ans)

def inin():
    return int(input())


def stin():
    return input()


def spin():
    return map(int, stin().split())


def lin():                           # takes array as input
    return list(map(int, stin().split()))


