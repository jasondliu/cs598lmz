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

def Main():
    for _ in range(int(input())):
        n = int(input())
        a = list(map(int, input().split()))
        a.sort()
        b = list(map(int, input().split()))
        b.sort()
        c = list(map(int, input().split()))
        c.sort()
        i = 0
        j = 0
        k = 0
        ans = 0
        while j < n:
            while i < n and a[i] <= b[j]:
                i
