import threading
threading.stack_size(2**27)
import sys
sys.setrecursionlimit(10**7)
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
from math import *
from collections import *
from queue import PriorityQueue
from bisect import bisect_left, bisect_right
from itertools import accumulate, permutations, combinations
from operator import itemgetter
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from datetime import datetime
# ---------------------------------------------------------------------
'''
problem : https://codeforces.com/contest/1354/problem/C
'''
# ---------------------------------------------------------------------

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    ans = 0
    for i in range(n):
        if a[i] > b[i]:
            ans += b[i]
