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
from itertools import *
from copy import deepcopy
from functools import reduce
from string import ascii_lowercase
from fractions import Fraction

def inp(): return int(input())
def inp_list(): return list(map(int, input().split()))
def inp_tuple(n): return tuple(map(int, input().split()))
def inp_str(): return input()
def new_list(n, x=0): return [x for _ in range(n)]
def new_tuple(n, x=0): return [x for _ in range(n)]
def print_list(a, sep=' ', end='\n'): print(sep.join(map(str,
