import threading
threading.stack_size(2**27)
import sys
sys.setrecursionlimit(10**7)
sys.stdin = open('inpy.txt', 'r')
sys.stdout = open('outpy.txt', 'w')
from math import *
from collections import *
from sys import stdin, stdout
from bisect import bisect_left, bisect_right
from heapq import heapify, heappop, heappush
from itertools import *
from copy import deepcopy
from decimal import *
from string import ascii_lowercase
from fractions import gcd
from functools import reduce
# import machine learning libraries here

#import numpy as np
#from scipy import stats
# automatically compute the number of points on the convex hull
#

def main():
    n = int(input())
    p = list(map(int, input().split()))
    for i in range(n):
        p[i] -= i + 1
    dp = [0] * n
    dp[0] = 1
