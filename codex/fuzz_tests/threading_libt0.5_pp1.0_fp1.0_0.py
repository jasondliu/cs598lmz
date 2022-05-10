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
 
#intializing heap
mod = 10 ** 9 + 7
 
#initializing temp
 
 
def calculate(a, b):
    return (a * b) % mod
 
 
def fpm(a, b):
    if b == 0:
        return 1
    elif b == 1:
        return a % mod
    else:
        return fpm(a, b // 2) * fpm(a, (b + 1) // 2) % mod
 
 
def main():
    for _ in range(int(input())):
        n = int(input())
        arr = list(map(int, input().split()))
        cnt = Counter(arr)
        l =
