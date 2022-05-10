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
 
blue, red, green, yellow, orange, purple = 30, 31, 32, 33, 34, 35
 
def printcolor(s, color):
    print("\033[1;%dm%s\033[1;m" % (color, s))
 
def gcd(a, b):
    if (a == 0):
        return b
    return gcd(b % a, a)
 
def sieve(n): 
    prime = [True for i in range(n + 1)]
    p = 2
    while (p * p <= n): 
        if (prime[p] == True): 
            for i in range(p * p, n + 1, p):
