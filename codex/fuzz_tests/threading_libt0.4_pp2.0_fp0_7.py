import threading
threading.stack_size(2**27)
import sys
sys.setrecursionlimit(10**7)
sys.stdin = open('inpy.txt', 'r')
sys.stdout = open('outpy.txt', 'w')
from math import *
from collections import *
from queue import PriorityQueue
from heapq import heapify, heappop, heappush
 
blue = []
red = []
ans = 0
 
def solve(blue, red, n, m):
    global ans
    if n == 0 and m == 0:
        ans += 1
        return
    if n == 0:
        red.pop()
        solve(blue, red, n, m-1)
        red.append(m)
    if m == 0:
        blue.pop()
        solve(blue, red, n-1, m)
        blue.append(n)
    if blue[-1] > red[-1]:
        blue.pop()
        solve(blue, red, n-1, m)
        blue.append(n)
    else:

