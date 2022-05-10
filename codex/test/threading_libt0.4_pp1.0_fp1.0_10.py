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
from itertools import permutations, combinations, product, accumulate, groupby
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from fractions import gcd
from random import randint


def sync_with_stdio(sync=True):
    if sync:
        stdin = sys.stdin
        sys.stdin = open('inpy.txt', 'r')
        stdout = sys.stdout
        sys.stdout = open('outpy.txt', 'w')

        return stdin, stdout
    else:
        sys.stdin = stdin
        sys.stdout = stdout


def process():
    pass


