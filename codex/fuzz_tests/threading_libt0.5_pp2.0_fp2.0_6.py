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
from itertools import permutations, combinations, product, accumulate, groupby
from copy import deepcopy
from operator import itemgetter
from string import ascii_lowercase, ascii_uppercase, digits
from fractions import gcd
from functools import reduce
def read(): return input().strip()
def read1(): return input().strip().split(' ')
def read2(): return list(map(int, input().strip().split(' ')))
def read_map(): return map(int, input().strip().split(' '))
def read_map1(n): return [list(map(int, input().strip().split(' '))) for _ in range(n)]
def read_map2(n, m): return [list
