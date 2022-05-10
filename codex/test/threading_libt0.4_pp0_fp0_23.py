import threading
threading.stack_size(2**27)
import sys
sys.setrecursionlimit(10**7)
sys.stdin = open('inpy.txt', 'r')
sys.stdout = open('outpy.txt', 'w')
from math import *
from collections import defaultdict, deque
from queue import Queue
from copy import deepcopy
ints = lambda x: int(x) - 1
p2D = lambda x: print(*x, sep="\n")
def WI(r): return [ints(x) for x in r.split()]
def WL(r): return [list(x) for x in r.split()]
def DS(): return input().split()
def I(): return int(input())
def S(): return input()
def MI(): return map(int, input().split())
def MS(): return map(str, input().split())
def LI(): return list(MI())
def LI_(): return [int(x)-1 for x in input().split()]
def StoI(): return [ord(x)-97 for x in input()]
