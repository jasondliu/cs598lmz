import threading
threading.stack_size(2**27)
import sys
sys.setrecursionlimit(10**7)
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
from math import *
from fractions import *
from collections import *
from queue import Queue
from heapq import heappush, heappop, heapify
 
 
def inp(): return int(input())
 
 
def inp_list(): return list(map(int, input().split()))
 
 
def lcm(a, b): return a*b // gcd(a, b)
 
 
cinp = inp_list
 
 
def solve(n, m):
    if n == 1:
        print(0)
        return
    if n == 2:
        print(m)
        return
    print(2*m)
 
 
test = 1
 
 
def multi_test():
    global test
    test = inp()
