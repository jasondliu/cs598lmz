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
 
def read_col(H, n_cols):
    '''
    H is number of rows
    n_cols is number of cols
    
    A列、B列が与えられるようなとき
    '''
    ret = [[] for _ in range(n_cols)]
    for _ in range(H):
        tmp = list(map(int, input().split()))
        for col in range(n_cols
