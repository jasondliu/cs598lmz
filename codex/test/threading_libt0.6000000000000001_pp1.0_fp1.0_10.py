import threading
threading.stack_size(2**27)
import sys
sys.setrecursionlimit(10**7)
sys.stdin = open('inpy.txt', 'r')
sys.stdout = open('outpy.txt', 'w')
from math import *
from collections import defaultdict, deque
from queue import Queue
from copy import deepcopy
from time import sleep
#import random
import heapq
from fractions import gcd
from bisect import bisect_left, bisect_right
inf = 10**20
mod = 10**9 + 7

int_input = lambda: int(input())
string_input = lambda: input()
multi_int_input = lambda: map(int, input().split())
multi_input = lambda: input().split()
list_input = lambda: list(map(int, input().split()))
string_list_input = lambda: list(string_input())
MOD = pow(10, 9)


test = int_input()
for _ in range(test):
    n = int_input()
    arr = list_input()
    ans
