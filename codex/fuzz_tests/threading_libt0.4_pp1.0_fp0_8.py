import threading
threading.stack_size(2**27)
import sys
sys.setrecursionlimit(10**7)
sys.stdin = open('inpy.txt', 'r')
sys.stdout = open('outpy.txt', 'w')
from math import *
from collections import defaultdict
from collections import deque
from queue import Queue
from heapq import heappush, heappop, heapify
from copy import deepcopy
from collections import Counter
from operator import itemgetter
from itertools import product, permutations, combinations
from bisect import bisect, bisect_left, bisect_right
from string import ascii_lowercase
from fractions import gcd
from random import randint


def time():
    return datetime.datetime.now().strftime("%H:%M:%S")


def print_result(ans):
    print('#' * 80)
    print(ans)
    print('#' * 80)
    print('\n' * 5)


def power(a, n):
    if n == 0:
        return 1

