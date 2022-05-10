import threading
threading.stack_size(2**27)
import sys
sys.setrecursionlimit(10**7)
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
from math import *
from queue import PriorityQueue
from collections import *
from itertools import *
from functools import *
from operator import *
from bisect import bisect_left, bisect
from string import ascii_lowercase
from fractions import gcd
from heapq import heappush, heappop
def lcm(a, b): return a*b // gcd(a, b)
cin = lambda: int(input())
cout = lambda x: print(x, end=' ')
coutln = lambda x: print(x, end='\n')
# coutln = lambda x: print(x)
# cout = lambda *args: print(*args, sep=' ', end=' ')
# coutln = lambda *args: print(*args, sep=' ', end='\n')
# coutln = lambda *args: print(*args
