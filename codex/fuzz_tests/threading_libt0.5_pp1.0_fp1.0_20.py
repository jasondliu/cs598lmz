import threading
threading.stack_size(2**27)
import sys
sys.setrecursionlimit(10**7)
sys.stdin = open('inpy.txt', 'r')
sys.stdout = open('outpy.txt', 'w')
from math import *
from collections import *
from queue import PriorityQueue
from bisect import bisect_left, bisect_right
from itertools import permutations, combinations
from copy import deepcopy

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    b = list(map(int, input().split()))
    b.sort()
    c = list(map(int, input().split()))
    c.sort()
    ans = 0
    for i in range(m):
        x = bisect_left(a, b[i])
        y = bisect_right(c, b[i])
        ans += x * (n - y)
    print(ans)


main()
