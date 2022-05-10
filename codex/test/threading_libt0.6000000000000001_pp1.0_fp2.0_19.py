import threading
threading.stack_size(2**27)
import sys
sys.setrecursionlimit(10**7)
sys.stdin = open('inpy.txt', 'r')
sys.stdout = open('outpy.txt', 'w')
from math import *
from bisect import bisect_left, bisect_right
from decimal import Decimal
from heapq import heappush, heappop
 
def inin():
    return int(input())
def stst():
    return input().replace('\n', '')
def spin():
    return map(int, stst().split())
def lin():                           #takes array as input
    return list(map(int, stst().split()))
def matrix(n):
    #matrix input
    return [list(map(int, input().split()))for i in range(n)]

################################################
def count2Dmatrix(i,list):
    return sum(c.count(i) for c in list)

