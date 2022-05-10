import threading
threading.stack_size(2**27)
import sys
import math
sys.setrecursionlimit(10**7)
sys.stdin = open('inpy.txt', 'r')
sys.stdout = open('outpy.txt', 'w')
from queue import PriorityQueue
from bisect import bisect_left, bisect_right
from math import floor,ceil
from heapq import heappush,heappop
import random
import time
from itertools import permutations,combinations,product,combinations_with_replacement
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, ascii_letters
from functools import reduce
import numpy as np
def inin():
    return int(input())
def stin():
    return input()
def spin():
    return map(int,stin().split())
def lin():                           #takes array as input
    return list(map(int,stin().split()))
