import threading
threading.stack_size(2**27)
import sys
sys.setrecursionlimit(10**7)
sys.stdin = open('/home/cris/Desktop/input.txt', 'r')
sys.stdout = open('/home/cris/Desktop/output.txt', 'w')


MOD = 1000000007

from math import log
from math import floor

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def lcm(a, b):
    return (a * b) // gcd(a, b)

def pow(a, b, mod=MOD):
    res = 1
    while b > 0:
        if b & 1:
            res = res * a % mod
        a = a * a % mod
        b >>= 1
    return res

def inv(n, mod=MOD):
    return pow(n, mod - 2, mod)

def ceil(a, b):
    return (a + b - 1) // b


