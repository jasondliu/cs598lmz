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
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from datetime import date

def init():
    return int(-1e9), int(1e9), []

def DFS(i, s, e, op):  # 시작점, 끝점, 연산자 리스트
    global Minv, Maxv
    if i == n:
        Minv = min(Minv, s)
        Maxv = max(Max
