import threading
threading.stack_size(2**27)
import sys
sys.setrecursionlimit(10**7)
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

from math import sqrt
from bisect import bisect_left
from collections import defaultdict
from random import randint
from time import time
from functools import wraps

primes = [2, 3]
isprime = [True] * (10**6 + 1)
isprime[0] = isprime[1] = False
for i in range(2, int(sqrt(10**6)) + 1):
    if isprime[i]:
        primes.append(i)
        for j in range(i**2, 10**6 + 1, i):
            isprime[j] = False

def solve(n):
    ans = 0
    for i in range(1, n+1):
        if i % 2 == 0:
            k = i // 2
        else:
            k = (i+1) // 2

