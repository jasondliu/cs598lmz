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
from itertools import permutations, combinations, product, accumulate
from operator import itemgetter, xor, add
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from datetime import datetime

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.sort()
    b.sort()
    ans = 0
    for i in range(n):
        for j in range(m):
            if a[i] > b[j]:
                ans += 1
                b[j] = float('
