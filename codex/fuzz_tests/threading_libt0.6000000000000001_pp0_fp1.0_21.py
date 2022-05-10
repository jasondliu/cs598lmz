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

#----------------------------------------------

def next_int(): return int(input())
def next_ints(): return [int(x) for x in input().split()]
def next_str(): return input()
def next_strs(): return [x for x in input().split()]
def next_chr(): return input()[0]
def next_chrs(): return [x[0] for x in input().split()]
def next_lines(n): return [input() for _ in range(n)]

#----------------------------------------------

def main():
    a, b = next_ints()

    ans = 0
   
