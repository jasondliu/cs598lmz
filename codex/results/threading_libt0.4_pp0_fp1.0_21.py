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
from itertools import accumulate, permutations, combinations
from operator import itemgetter
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from fractions import gcd
from random import randint


mod = 10 ** 9 + 7
inf = float('inf')
ninf = -float('inf')
 
#---------------------------_/\_Main Program Start Here_/\_------------------
def solve(n):
    if n == 1:
        return n
    if n % 2 == 0:
        return 2
    for i in range(3, int(sqrt(n)) + 1, 2):
        if n % i == 0:
            return i
    return n

