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
import time
import heapq

def main():
    n, m, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a = [0] + a
    b = [0] + b
    for i in range(1, n + 1):
        a[i] += a[i - 1]
    for i in range(1, m + 1):
        b[i] += b[i - 1]
    ans = 0
    j = m
    for
