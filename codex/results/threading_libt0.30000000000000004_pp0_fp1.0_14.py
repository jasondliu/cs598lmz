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
from itertools import permutations, combinations, product, accumulate
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from datetime import date

def shift_left(L): return [L[1], L[2], L[0]]
def shift_right(L): return [L[2], L[0], L[1]]

def string(L): return ''.join(L)

def check():
    global ans
    global a, b, c
    if a == b == c:
        ans = '0'
        return
    if a == b:
        ans = 'C'
        return
   
