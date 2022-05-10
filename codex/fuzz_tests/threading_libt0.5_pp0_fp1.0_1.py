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
 
def fast_exp(base, exp):
    result = 1
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        base = (base * base) % mod
        exp = exp // 2
    return result % mod
 
def modinv(a, m):
    return fast_exp(a, m - 2)
 
def nCr(n, r, p):
    numer = denom = 1
    for i in range(1, r + 1):
        numer = (numer * (n - i + 1)) % p
        denom = (denom
