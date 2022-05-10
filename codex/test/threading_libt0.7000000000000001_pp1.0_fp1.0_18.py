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
from itertools import accumulate, permutations, combinations
from operator import itemgetter
from copy import deepcopy
import random
inf = 10**20
mod = 1000000007

def LOAD(): return map(int, input().split())
def LOAD_S(): return list(input())
def LOAD_A(n): return [int(i) for i in input().split()]
def LOAD_AR(n, m): return [LOAD_A(m) for i in range(n)]


class WeightedUnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.rank = [0] * n
