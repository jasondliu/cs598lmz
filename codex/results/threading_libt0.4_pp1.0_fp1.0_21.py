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
 
blue, red, white = '0', '1', '.'
 
def fast_exp(base, power):
    result = 1
    while power > 0:
        if power % 2 == 1:
            result = (result * base) % mod
        power = power // 2
        base = (base * base) % mod
    return result
 
def modinv(n, p):
    return fast_exp(n, p - 2)
 
def solve(a, b, c, d):
    if a + b == c + d:
        return 'YES'
    if a + b == c - d:
        return 'YES'
    if a - b == c + d:
       
