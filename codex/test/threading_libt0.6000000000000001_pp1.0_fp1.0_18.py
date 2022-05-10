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
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from bisect import bisect, bisect_left
from fractions import gcd
from heapq import heappush, heappop
from functools import reduce
def main():
    n, k = map(int, input().split())
    s = input()
    if k == 1:
        print(n)
        exit()
    ans = 0
    for i in range(n):
        if s[i] == '1':
            continue
        j = i
        cnt = 0
