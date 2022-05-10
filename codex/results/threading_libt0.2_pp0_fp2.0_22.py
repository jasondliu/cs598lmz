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
 
blue, red, green = '0', '1', '2'
 
def read(): return stdin.readline().strip()
def write(s): stdout.write(str(s) + '\n')
def end(): exit()
 
def get_ints(): return list(map(int, read().split()))
def get_int(): return int(read())
def get_strs(): return list(read().split())
def get_str(): return read()
def get_floats(): return list(map(float, read().split()))
def get_float(): return float(read())
 
def get_grid(h, w): return [list(read()) for _ in range(h)]
