import threading
threading.stack_size(2**27)
import sys
sys.setrecursionlimit(10**7)
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
from math import *
from queue import PriorityQueue
from heapq import heapify, heappop, heappush
 
mod = 10 ** 9 + 7
inf = float('inf')
eps = 10 ** -7
 
def inp():
    return int(input())
def inlt():
    return list(map(int, input().split()))
def insr():
    s = input()
    return list(s[:len(s) - 1])
def invr():
    return map(int, input().split())
 
def solve(n, x, y):
    if n == 2 and x == 0 and y == 0:
        return 1
    if y == 0 and x > 0:
        return 0
