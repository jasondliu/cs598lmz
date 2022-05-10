import threading
threading.stack_size(2**27)
import sys
sys.setrecursionlimit(10**7)
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
from math import *
from collections import *
from queue import PriorityQueue
from bisect import bisect_left, bisect_right
from itertools import permutations
from functools import reduce
def inp(): return int(input())
def inp_list(): return list(map(int, input().split()))
def inp_string(): return input()
def lcm(a,b): return a*b // gcd(a,b)
 
MOD = 1000000007
 
def solve(n, k):
    if k == 1:
        return n
    if n == 1:
        return 0
    if n == 2:
        return 1
    if n == 3:
        return 2
    if n == 4:
        return 3
    if n == 5:
        return 4
    if n == 6:
        return 5

