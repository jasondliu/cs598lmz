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
from itertools import *
from copy import deepcopy

#int_input=lambda : int(input())
#string_input=lambda : input()
#multi_int_input =lambda : map(int, input().split())
#multi_input = lambda : input().split()
#list_input=lambda : list(map(int,input().split()))
#string_list_input=lambda: list(input())
MOD = pow(10,9)+7

test = int(input())

for _ in range(test):
    n = int(input())
    arr = list(map(int,input().split()))
    arr.sort()
    max_val = arr[-1]
    min
