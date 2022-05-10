import threading
threading.stack_size(2**27)
import sys
sys.setrecursionlimit(10**7)
sys.stdin = open('inpy.txt', 'r')
sys.stdout = open('outpy.txt', 'w')
from math import *
from collections import deque, Counter
from collections import defaultdict
from heapq import heappush, heappop
from itertools import permutations, accumulate
import random
from operator import itemgetter
from time import time
def main():
    for _ in range(int(input())):
        n, m = map(int, input().split())
        s = []
        for i in range(n):
            s.append(input())
        for i in range(m):
            c = 0
            for j in range(n):
                if s[j][i] == '1':
                    c += 1
            if c == 0:
                print(-1)
                break
            elif c == 1:
                print(1)
                break
            elif c == 2:
                print(2)
                break
