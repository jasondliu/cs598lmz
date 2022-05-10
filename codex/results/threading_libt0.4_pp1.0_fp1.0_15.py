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
inf = float('inf')
eps = 10 ** -7
 
def inp(): return int(input())
def inp_1(): return int(input()) - 1
def inp_int(): return int(input())
def inp_float(): return float(input())
def inps_line(): return input().split(' ')
def inps_ints(): return list(map(int, input().split(' ')))
def inps_strs(): return list(input().split(' '))
def inpl_line(): return list(map(int, input().split(' ')))
def inpl_ints(): return [int(x) for x in input().split(' ')]
def str
