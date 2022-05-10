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

def printgrid(arr):
    for i in range(n):
        print(*arr[i])
    print()

def fast_exp(base, exp):
    res=1
    while(exp>0):
        if(exp%2==1):
            res=(res*base)%mod
        base=(base*base)%mod
        exp=exp//2
    return res%mod

def gcd(a, b):
    if(a==0):
        return b 
    return gcd(b%a,a)

def sieve(n): 
    prime=[True for i in range(n+1)]
    p=2
    while(p*p<=
