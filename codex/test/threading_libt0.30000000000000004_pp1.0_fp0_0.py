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

mod = 10 ** 9 + 7
inf = float('inf')
ninf = -float('inf')
 
#----------------------------------------#
def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    cnt = 0
    for i in range(n):
        cnt += b[a[i] - 1]
        if i > 0 and a[i] == a[i - 1] + 1:
            cnt += c[a[i - 1] - 1]
    print(cnt)


    return

