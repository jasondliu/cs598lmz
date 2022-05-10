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

mod = 998244353
inf = 10**9

def read():
    return int(input())

def read_arr():
    return list(map(int, input().split()))

def read_map():
    return map(int, input().split())

def read_tuple(type=int):
    return tuple(map(type, input().split()))

def read_mat(typ=int):
    return [list(map(typ, input().split())) for _ in range(N)]

def read_str():
    return input()

def read_str_arr():
    return list(input())

def read_str
