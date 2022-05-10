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
 
blue, red, green = '01#'
 
def stdin_getint():
    return int(stdin_getstr())
 
def stdin_getstr():
    return input()
 
def stdin_getlist():
    return list(map(int, stdin_getstr().split()))
 
def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m
 
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g,
