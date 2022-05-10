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
from itertools import permutations, combinations, product, accumulate
from operator import itemgetter, xor, add
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from datetime import datetime

def DEBUG():
    return False

if DEBUG():
    import numpy as np
    import random


def read():
    return sys.stdin.readline().strip()


def read_int():
    return int(read())


def read_ints():
    return list(map(int, read().split()))


def read_a_int():
    return read_ints()


