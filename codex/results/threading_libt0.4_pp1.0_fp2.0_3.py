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

#---------------------------_/\_Main Program Start Here_/\_------------------
def main():
    n = int(input())
    arr = []
    for i in range(n):
        arr.append(list(map(int, input().split())))
    arr.sort()
    arr.sort(key=lambda x: x[1])
    for i in range(n):
        print(arr[i][0], arr[i][1])


main()
