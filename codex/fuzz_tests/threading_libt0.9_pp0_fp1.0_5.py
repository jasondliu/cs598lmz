import threading
threading.stack_size(2**27)
import sys
sys.setrecursionlimit(10**7)
sys.stdin = open('inpy.txt', 'r')
sys.stdout = open('outpy.txt', 'w')
from math import *
from bisect import *
from heapq import *
from time import time
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
def calculatencr(n,r):
    # calculate ncr using math.factorial()
    return math.factorial(n) / math.factorial(r) / math.factorial(n-r)

def nCr(n,r):
    # use table increasing the size with demand
    global n
