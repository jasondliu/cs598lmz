import threading
threading.stack_size(2**27)
import sys
# sys.setrecursionlimit(10**7)
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
from math import *
inf = 10**9
mod = 10**9 + 7


def InverseSquare(n):
    f = [1] * (n + 1)
    for i in range(2, n + 1):
        f[i] = f[i - 1] * i % mod
    return f


f = InverseSquare(200000)
finv = [pow(f[i], mod - 2, mod) for i in range(200000 + 1)]
finv = [1] + finv


def nCr(n, r):
    if n < r:
        return 0
    return f[n] * finv[r] * finv[n - r] % mod
print(nCr(1e5, nCr(1e5, 1e5)))

print((0.5)**1e5)
