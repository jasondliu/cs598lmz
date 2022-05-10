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
from itertools import *
from copy import deepcopy
import random
inf = 10**9
mod = 10**9 + 7

def inp():
    return int(input())
def stinp():
    return [int(i) for i in input().split()]
def spinp():
    return [int(i) for i in input().split()]
def linp():
    return [i for i in input().split()]
def linps(n):
    return [input() for _ in range(n)]
def arr2d(n, m):
    return [[0 for _ in range(m)] for _ in range(n)]
