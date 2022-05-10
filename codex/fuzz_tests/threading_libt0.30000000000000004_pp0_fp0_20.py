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
from fractions import gcd
def boost():
    global chk1
    chk1 = list(map(int, input().split()))
def dec(c):
    global chk1
    if(c == '+'):
        chk1[0] += 1
    elif(c == '-'):
        chk1[0] -= 1
    elif(c == '>'):
        chk1[1] += 1
    elif(c == '<'):
