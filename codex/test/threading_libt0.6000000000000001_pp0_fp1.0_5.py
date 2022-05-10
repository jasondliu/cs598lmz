import threading
threading.stack_size(2**27)
import sys
sys.setrecursionlimit(10**7)
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
from math import *
from collections import defaultdict
from collections import deque
from collections import OrderedDict
from functools import reduce
from time import time
import itertools
def I(): return int(input())
def F(): return float(input())
def SS(): return input()
def LI(): return [int(x) for x in input().split()]
def LI_(): return [int(x)-1 for x in input().split()]
def LF(): return [float(x) for x in input().split()]
def LSS(): return input().split()
def IS(n): return [I() for _ in range(n)]
def FS(n): return [F() for _ in range(n)]
def LIS(n): return [LI() for _ in range(n)]
