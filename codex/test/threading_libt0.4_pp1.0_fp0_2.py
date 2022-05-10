import threading
threading.stack_size(2**27)
import sys
sys.setrecursionlimit(10**7)
sys.stdin = open('inpy.txt', 'r')
sys.stdout = open('outpy.txt', 'w')
from math import floor, sqrt, log
from collections import Counter, deque
from fractions import gcd
from sys import stdin, stdout
from bisect import bisect_left, bisect_right
read = lambda: stdin.readline().strip()
pyl = lambda: list(map(int, read().split()))
prl = lambda: list(map(float, read().split()))
n = int(read())
a = pyl()
b = pyl()

def solve(n, a, b):
    a.sort()
    b.sort()
    b.reverse()
    ans = 0
    for i in range(n):
        ans += a[i] * b[i]
    return ans

print(solve(n, a, b))
