import threading
threading.stack_size(2**27)
import sys
sys.setrecursionlimit(10**7)
sys.stdin = open('inpy.txt', 'r')
sys.stdout = open('outpy.txt', 'w')
from math import *
from collections import *
from queue import Queue
from heapq import heappush, heappop
_ct = 0
# def pr():
#     global _ct
#     _ct+=1
#     print(_ct,end=' ')
def inp():
    return(int(input()))
def inlt():
    return(list(map(int,input().split())))
def insr():
    s = input()
    return(list(s[:len(s) - 1]))
def invr():
    return(map(int,input().split()))

class node:
    def __init__(self, w=0, h=0, x=0, y=0):
        self.w = w
        self.h = h
        self.x = x
        self.y =
