import threading
threading.stack_size(2**27)
import sys
sys.setrecursionlimit(10**5)
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

from collections import defaultdict, deque
from bisect import bisect_left, bisect_right
from math import ceil, log, log2
from fractions import Fraction
from random import randrange, randint, shuffle, choice
from time import time
from heapq import heappop, heappush, heapify
from copy import deepcopy
from itertools import product
from operator import itemgetter

from hashlib import md5


def get_hash(key):
    h = md5(key.encode()).hexdigest()
    return h

def get_hash2(key):
    h = md5(key.encode()).hexdigest()
    return h

def get_char(h):
    if h < 'a':
        return chr(ord('z') - int(h, 16)%26)

