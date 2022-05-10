import threading
threading.stack_size(2**27)
import sys
sys.setrecursionlimit(10**7)
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
from math import *
from collections import *
from queue import PriorityQueue
from heapq import heapify, heappop, heappush
 
mod = 10 ** 9 + 7
inf = 10 ** 18
eps = 10 ** -7
 
# Start code
 
 
def main():
    n, m = map(int, input().split())
    d = [0] * n
    for i in range(m):
        a, b = [int(i) for i in input().split()]
        a -= 1
        b -= 1
        d[a] += 1
        d[b] += 1
    for i in range(n):
        if d[i] % 2 != 0:
            print("NO")
            return 0
    print("YES")
 
 
 
 
if __name__ == '__main__':
