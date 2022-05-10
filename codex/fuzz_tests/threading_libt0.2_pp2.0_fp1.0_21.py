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
def stst(): return input().strip()
def get_list(): return list(map(int, input().split()))
def get_row(H): return [int(input()) for _ in range(H)]
def get_matrix(H): return [get_row(H) for _ in range(H)]
def prr(num): return print(num, end=' ')
def prrr(num1, num2): return print(num1
