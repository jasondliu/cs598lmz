import threading
threading.stack_size(2**27)
import sys
sys.setrecursionlimit(10**7)
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
from math import *
from collections import *
from queue import PriorityQueue
from bisect import bisect_left, bisect_right
from itertools import product, combinations,permutations
from copy import deepcopy
int1 = lambda x: int(x) - 1
pii = lambda x: print(*x)
def dp(ind,last):
  if ind == n:
    return 0
  if dp_[ind][last] != -1:
    return dp_[ind][last]
  ans = dp(ind+1,last)
  if last == -1 or (a[ind] > a[last] and b[ind] < b[last]):
    ans = max(ans,1+dp(ind+1,ind))
  dp_[ind][last] = ans
  return ans
