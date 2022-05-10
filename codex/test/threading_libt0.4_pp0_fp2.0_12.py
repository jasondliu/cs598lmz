import threading
threading.stack_size(2**27)
import sys
sys.setrecursionlimit(10**7)
sys.stdin = open('inpy.txt', 'r')
sys.stdout = open('outpy.txt', 'w')
from math import *
from collections import *
from collections import deque,Counter
from decimal import Decimal
#sys.stdin = open('input.txt', 'r')
#sys.stdout = open('output.txt', 'w')
#sys.stdin = open('inpy.txt', 'r')
#sys.stdout = open('outpy.txt', 'w')
from fractions import *
from heapq import *
from bisect import *
from math import *
inf = int(1e18)
mod = 1000000007

n, k = map(int, input().split())
a = list(map(int, input().split()))
for i in range(n):
    a[i] = a[i] - 1
a.sort()
