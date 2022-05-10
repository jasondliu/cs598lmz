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
def inpl(): return list(map(int, input().split()))
def inpls(): return list(input().split())

N, X = inpl()
L = inpl()

cnt = 1
d = 0
for l in L:
    d += l
    if d <= X:
        cnt += 1
    else:
        break
print(cnt)
