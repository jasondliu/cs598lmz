import threading
threading.stack_size(2**27)
import sys
sys.setrecursionlimit(10**6)
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
from math import floor,ceil,sqrt,factorial,log
from heapq import heappop, heappush, heappushpop
from collections import Counter,defaultdict,deque
from itertools import accumulate,permutations,combinations,product,combinations_with_replacement
from bisect import bisect_left,bisect_right
from decimal import Decimal
inf = float('inf')
import math 
mod = 1000000007
mod = 998244353
import time
start = time.time()#odometer starts
#print(time.time()-start)
f= open('input.txt' ,'r')
#print(time.time()-start)
d={}
for line in f.readlines():
    line=line.split()
    #print(line)
