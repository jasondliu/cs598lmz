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
 
blue, red, green = '0123456789ABCDEF'
MOD = 1000000007
 
show_flg = False
#show_flg = True
 
def print(*args, **kwargs):
    if show_flg:
        print(*args, **kwargs)
 
def show(*args, **kwargs):
    if show_flg:
        show(*args, **kwargs)
 
def get_primes(n):
    primes = []
    is_prime = [True] * (n + 1)
    is_prime[0] = False
    is_prime[1] = False
