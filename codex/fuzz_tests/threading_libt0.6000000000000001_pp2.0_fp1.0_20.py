import threading
threading.stack_size(2**27)
import sys
sys.setrecursionlimit(10**7)
sys.stdin = open('inpy.txt', 'r')
sys.stdout = open('outpy.txt', 'w')
from math import *
from collections import *
from queue import PriorityQueue
from bisect import bisect_left, bisect_right
from itertools import accumulate,permutations,combinations,product,combinations_with_replacement
from copy import deepcopy
int(input())
n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
ans=0
for i in range(1<<n):
    s=0
    for j in range(n):
        if (i>>j)&1:
            s+=a[j]
    ans=max(ans,s)
    for j in range(m):
        if s+b[j]<=ans:
            ans=max(ans,s+b[j])

