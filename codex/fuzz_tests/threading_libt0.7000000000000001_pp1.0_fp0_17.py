import threading
threading.stack_size(2**27)
import sys
sys.setrecursionlimit(10**7)
sys.stdin = open('inpy.txt', 'r')
sys.stdout = open('outpy.txt', 'w')
from sys import stdin, stdout
import bisect            #c++ upperbound
import math
import heapq
i_m=9223372036854775807
def invr(a):
    return pow(a, i_m-2, i_m)

mod = 1000000007
 
n = int(input())

s = [int(x) for x in input().split()]
s = sorted(list(set(s)))

if len(s) > 3:
    print("NO")
    exit()

if len(s)==1:
    print("YES")
    print(s[0], s[0], s[0])
    exit()

if len(s)==2:
    if s[1]-s[0]%2==0:
        print("YES")
        print
