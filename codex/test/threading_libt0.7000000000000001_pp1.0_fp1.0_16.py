import threading
threading.stack_size(2**27)
import sys
sys.setrecursionlimit(10**7)
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
from queue import Queue
from bisect import bisect_left, bisect_right
from math import floor, ceil, gcd, inf
from collections import Counter, defaultdict
from itertools import accumulate, permutations, combinations, product
from operator import itemgetter, xor
from string import ascii_lowercase, ascii_uppercase, digits
from fractions import Fraction
mod = 10 ** 9 + 7
def sieve_list(n):
    sieve = [True] * (n + 1)
    sieve[0] = False
    sieve[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        pointer = i * 2
        while pointer <= n:
            sieve[pointer] = False
            pointer += i
    primes = []
