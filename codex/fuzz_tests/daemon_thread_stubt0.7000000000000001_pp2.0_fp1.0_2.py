import sys, threading

def run():
  sys.stdin = os.fdopen(sys.stdin.fileno(), 'r', 0)
  #sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)
  #sys.stderr = os.fdopen(sys.stderr.fileno(), 'w', 0)

#threading.Thread(target=run).start()

from math import *
from collections import *
from heapq import *
from bisect import *
from string import *
from fractions import Fraction
from decimal import Decimal
from itertools import *
from random import *

def solve():
  N, K = map(int, raw_input().strip().split())
  s = sorted(map(int, raw_input().strip().split()))
  #print s

  ans = 0
  for i in range(N):
    if s[i] < 0:
      continue
    #print i
    ans += 1
    if K > 1:
      for j in range(i+1, N):
        if ceil(float
