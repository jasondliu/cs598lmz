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

MOD = 1000000007

def read():
    return int(input())
def read_list():
    return list(map(int, input().split()))
def read_map():
    return map(int, input().split())
def read_pair():
    return [int(x) for x in input().split()]
def read_string():
    return input()
def new_stack():
    return [int(x) for x in input().split()]

def solve(n, k):
    if n == 0:
        return 0
    if k == 0:
        return n
    if n == 1:
        return 1
