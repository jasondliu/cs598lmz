import threading
threading.stack_size(2**27)
import sys
sys.setrecursionlimit(10**7)
sys.stdin = open('inpy.txt', 'r')
sys.stdout = open('outpy.txt', 'w')
from math import *
from collections import *
from collections import deque,Counter
from itertools import combinations,permutations
from itertools import accumulate
import operator as op
from string import ascii_uppercase, ascii_lowercase
from heapq import heapify, heappop, heappush, heappushpop
from bisect import bisect_left, bisect_right
from functools import reduce
def main():
    n = int(input())
    a = list(map(int,input().split()))
    a.sort()
    if n % 2 == 0:
        print(a[n//2] - a[n//2 - 1] + 1)
    else:
        print(0)
if __name__ == '__main__':
    threading.Thread(target=main).start()
