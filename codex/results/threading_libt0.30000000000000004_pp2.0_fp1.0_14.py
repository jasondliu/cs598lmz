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
from itertools import permutations, combinations
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from functools import reduce
def read():
  return int(input())
def read_arr():
  return list(map(int, input().split()))
def read_arr_list():
  return [list(map(int, input().split())) for _ in range(N)]

def solve(n):
  if n == 0:
    return 'INSOMNIA'
  seen = set()
  i = 1
  while len(seen) < 10:
    num = n * i
    while num > 0:
      seen.add(num % 10
