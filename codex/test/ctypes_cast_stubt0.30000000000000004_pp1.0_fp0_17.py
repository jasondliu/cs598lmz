import ctypes
ctypes.cast(0, ctypes.py_object)

#import sys
#sys.setrecursionlimit(100000)

#import threading
#threading.stack_size(67108864)
#sys.setrecursionlimit(2 ** 20)

#sys.stdin = open('inpy.txt', 'r')
#sys.stdout = open('outpy.txt', 'w')

from sys import stdin, stdout
import bisect            #c++ upperbound
import math
import heapq
i_m=9223372036854775807
def inin():
    return int(input())
def stin():
    return input()
def spin():
    return map(int,stin().split())
def lin():                           #takes array as input
    return list(map(int,stin().split()))
def matrix(n):
    #matrix input
    return [list(map(int,input().split()))for i in range(n)]

################################################
