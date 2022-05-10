import threading
threading.stack_size(2**27)
import sys
sys.setrecursionlimit(10**7)
sys.stdin = open('inpy.txt', 'r')
sys.stdout = open('outpy.txt', 'w')
from math import gcd
from collections import Counter, deque, defaultdict
from queue import Queue
from copy import deepcopy
from time import time
import numpy as np
from fractions import Fraction
from random import randint
inf = 10**20
gosa = 1.0 / 10**10
mod = 10**9+7
def pd(n, k): return float((n * n * n * n * n * n * n * n * n)) % k
def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x)-1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()

