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
 
blue, red, green = 0, 1, 2
 
def read_int():
    return int(input())
def read_ints():
    return list(map(int, input().split()))
def read_str():
    return input()
def read_strs():
    return list(input().split())
 
def solve():
    n, m = read_ints()
    a = read_ints()
    b = read_ints()
    c = read_ints()
    d = read_ints()
    e = read_ints()
    f = read_ints()
    g = read_ints()
    h = read_ints()
    i = read_ints()
    j =
