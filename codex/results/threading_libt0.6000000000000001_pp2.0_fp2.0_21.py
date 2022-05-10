import threading
threading.stack_size(2**27)
import sys
sys.setrecursionlimit(10**7)
sys.stdin = open('inpy.txt', 'r')
sys.stdout = open('outpy.txt', 'w')
from math import *
from collections import deque, Counter
from collections import defaultdict as dd
from itertools import combinations, permutations
from itertools import accumulate
from operator import itemgetter
import heapq
from bisect import bisect_left, bisect_right
from copy import deepcopy
ints = lambda x: list(map(int, x.split()))
inp=lambda: int(input())
st=lambda: input()
lst=lambda: list(map(int,input().split()))
arr=lambda: list(map(st,input().split()))
def init():
    n,k=lst()
    p=lst()
    s=st()
    return n,k,p,s

def main():
    n,k,p,s=init()
    fin=[]
    for i
