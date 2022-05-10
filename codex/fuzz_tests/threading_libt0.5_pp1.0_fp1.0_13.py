import threading
threading.stack_size(2**27)
import sys
import math
sys.setrecursionlimit(10**7)
sys.stdin = open('inpy.txt', 'r')
sys.stdout = open('outpy.txt', 'w')
from fractions import gcd
def LCM (a, b): return a * b // gcd(a, b)
sys.stdin = open('inpy.txt', 'r')
sys.stdout = open('outpy.txt', 'w')
from fractions import gcd
def LCM (a, b): return a * b // gcd(a, b)
def SieveOfEratosthenes(n): 
    prime = [True for i in range(n+1)] 
    p = 2
    while (p * p <= n): 
        if (prime[p] == True): 
            for i in range(p * p, n+1, p): 
                prime[i] = False
        p += 1
    f = []
    for p in range(2, n): 
        if prime
