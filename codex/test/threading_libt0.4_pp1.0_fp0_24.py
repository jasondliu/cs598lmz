import threading
threading.stack_size(2**27)
import sys
sys.setrecursionlimit(10**7)
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
from math import *
from queue import PriorityQueue
from collections import deque
from bisect import bisect_left, bisect_right
input = sys.stdin.readline
 
mod = 998244353
 
def inp():
    return int(input())
def inps():
    return input()
def inpl():
    return list(map(int, input().split()))
def insr():
    s = input()
    return list(s[:len(s) - 1])
def invr():
    return map(int, input().split())
 
 
n, m = invr()
 
a = inpl()
a.sort()
 
b = inpl()
b.sort()
 
c = inpl()
c.sort()
 
ans = 0
 
