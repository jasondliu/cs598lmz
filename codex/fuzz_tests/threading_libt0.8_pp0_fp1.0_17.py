import threading
threading.stack_size(2**27)
import sys
sys.setrecursionlimit(10**7)
sys.stdin = open('inpy.txt', 'r')
sys.stdout = open('outpy.txt', 'w')
from bisect import insort, bisect_left
from math import floor, log, log2
from fractions import gcd
from copy import deepcopy
from functools import reduce
from decimal import Decimal
inf = inf
gcd = gcd


def inin():
    return int(input())


def stin():
    return input()


def spin():
    return map(int, stin().split())


def lin():                           # takes array as input
    return list(map(int, stin().split()))


def matrix(n):
    #matrix input
    return [list(map(int, input().split()))for i in range(n)]

################################################


def count2Dmatrix(i, list):
    return sum(c.count(i) for c in list)


def modinv(
