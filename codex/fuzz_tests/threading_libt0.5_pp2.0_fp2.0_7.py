import threading
threading.stack_size(2**27)
import sys
sys.setrecursionlimit(10**7)
sys.stdin = open('inpy.txt', 'r')
sys.stdout = open('outpy.txt', 'w')
from math import *
from collections import defaultdict
from collections import deque
from collections import Counter
from time import time
def lcm(a, b):
    return a * b // gcd(a, b)
fast_reader = lambda: map(int, input().split())
fast_writer = lambda x: print(*x, sep=' ')

######################################################################

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    a.sort()
    b.sort()
    c.sort()
    ans = 0
    for i in b:
        ans += (bisect.bisect_left(a, i) * (n - bisect.
