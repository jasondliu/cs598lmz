import threading
threading.stack_size(2**27)
import sys
sys.setrecursionlimit(10**7)
sys.stdin = open('inpy.txt', 'r')
sys.stdout = open('outpy.txt', 'w')
from math import *
from collections import *
from sys import stdin, stdout
from bisect import bisect_left, bisect_right
from itertools import accumulate
input = stdin.readline
pii pair;
#-------------------Šaráv Ganguly-------------------#

def read():
    return stdin.readline().strip()
def write(x):
    stdout.write(str(x))
def endline():
    stdout.write("\n")
def readarr(sep=None):
    return list(map(int, read().split(sep)))
def writearr(arr, sep=None):
    stdout.write(sep.join(str(x) for x in arr))
def remove(x):
    x.pop()
def pop(x):
    return x.pop()
