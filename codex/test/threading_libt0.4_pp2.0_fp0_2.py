import threading
threading.stack_size(2**27)
import sys
sys.setrecursionlimit(10**7)
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
from math import *
from collections import *
from queue import Queue
from heapq import heappush, heappop, heapify
 
my_file = open("a.in", "r")
# my_file = sys.stdin
input = lambda: my_file.readline().strip()
# sys.stdin = open('input.txt','r')
# sys.stdout = open('output.txt','w')
mod = pow(10, 9) + 7
# mod = 998244353
inf = pow(10, 15)
# inf = float('inf')
# float('inf')
# 10**9 +7
# 10**9 +9


def power(x, y, m):
    if (y == 0):
        return 1
