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
    return [int(x) for x in input().split()]
 
def read_str():
    return input()
 
def read_strs():
    return [x for x in input().split()]
 
def read_str_list():
    return [x for x in input().splitlines()]
 
def read_matrix(H):
    '''
    H is number of rows
    '''
    return [list(map(int, input().split())) for _ in range(H)]
