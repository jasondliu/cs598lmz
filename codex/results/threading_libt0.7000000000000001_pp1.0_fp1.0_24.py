import threading
threading.stack_size(2**27)
import sys
sys.setrecursionlimit(10**7)
sys.stdin = open('inpy.txt', 'r')
sys.stdout = open('outpy.txt', 'w')
from math import gcd
from fractions import Fraction
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations

def main():
    n = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    if A[0] != B[0]:
        print(0)
    else:
        L = [A[0]]
        i = 1
        while i < n:
            if A[i] == B[i]:
                L.append(A[i
