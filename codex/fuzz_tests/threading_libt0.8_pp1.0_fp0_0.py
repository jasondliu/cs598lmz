import threading
threading.stack_size(2**27)
import sys
sys.setrecursionlimit(10**7)
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
from math import *
from collections import *
from queue import Queue
from heapq import heappush, heappop, heapify
 
mod = 10 ** 9 + 7
inf = 10 ** 18
eps = 10 ** -7
 
def inp(): return int(input())
def inp_1(): return int(input()) - 1
def inp_2(): return list(map(int, input().split()))
def inl_2(): return [int(input())-1 for _ in range(2)]
def ins_2(): return [list(map(int, input().split())) for _ in range(2)]
def str_list(): return list(input())
def vec(a, b, c): return [a*b//gcd(a, b), a*c//gcd(a, c), b*c//gcd(b,
