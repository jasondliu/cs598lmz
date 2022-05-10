import threading
threading.stack_size(2**27)
import sys
sys.setrecursionlimit(10**7)
sys.stdin = open('inpy.txt', 'r')
sys.stdout = open('outpy.txt', 'w')
from math import *
from collections import *
from queue import PriorityQueue
from heapq import heappush, heappop

MOD = 10 ** 9 + 7

def MI(): return map(int, input().split())
def MI0(): return map(lambda s: int(s) - 1, input().split())
def LI(): return list(MI())
def II(): return int(input())
def LS(): return input().split()

def main():
    n, m = MI()
    a = LI()
    a.sort()
    cnt = 0
    for i in range(m):
        if a[i] < 0:
            cnt += abs(a[i])
    print(cnt)

main()
