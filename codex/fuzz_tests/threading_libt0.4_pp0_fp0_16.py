import threading
threading.stack_size(2**27)
import sys
sys.setrecursionlimit(10**7)
sys.stdin = open('inpy.txt', 'r')
sys.stdout = open('outpy.txt', 'w')
from math import *
from collections import *
from queue import PriorityQueue
from heapq import heapify, heappop, heappush
 
blue, red, green = '01.#'
 
def stdin_getint():
    return int(input())
 
def stdin_getints():
    return list(map(int, input().split()))
 
def stdin_getstr():
    return input()
 
def stdin_getstrs():
    return list(input().split())
 
def stdin_getgrid(H):
    return [stdin_getstr() for _ in range(H)]
 
def stdin_getints_col(H, n_cols):
    return [stdin_getints() for _ in range(H)]
 
def lcm(a, b):
    return
