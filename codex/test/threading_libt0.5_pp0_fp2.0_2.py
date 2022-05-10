import threading
threading.stack_size(2**27)
import sys
sys.setrecursionlimit(10**7)
sys.stdin = open('inpy.txt', 'r')
sys.stdout = open('outpy.txt', 'w')
from math import floor, sqrt, log
from collections import Counter, defaultdict
from fractions import Fraction
from random import randrange, randint, choice
from itertools import permutations, combinations, product, accumulate, cycle
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from bisect import bisect, bisect_left, bisect_right
from functools import reduce
def scan(): return input()
def i(): return int(input())
def s(): return input()
def ii(): return map(int, input().split())
def li(): return list(map(int, input().split()))
def ls(): return list(input().split())
def mii(): return map(lambda x: int(x) - 1, input().split())
