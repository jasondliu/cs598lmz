import threading
threading.stack_size(2**27)
import sys
sys.setrecursionlimit(10**7)
sys.stdin = open('inpy.txt', 'r')
sys.stdout = open('outpy.txt', 'w')
from collections import Counter, deque, defaultdict
from datetime import datetime
from functools import lru_cache, wraps
from heapq import heappush, heappop, heapify
from itertools import accumulate, product, permutations, combinations

def main():
    s = input()
    t = input()
    if s == t[:-1]:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()
