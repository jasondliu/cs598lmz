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
from itertools import permutations, combinations, product, accumulate, combinations_with_replacement
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from functools import reduce
def inin(): return int(input())
def stst(): return input().split()
def get_min(in_): return(min(in_))
def get_max(in_): return(max(in_))
def random_int_list(): return random.sample(range(1, int(input('Enter the upper range : '))), int(input('Enter the length of list : ')))
def ii(): return int(input())
def si(): return input()
def dillist(
