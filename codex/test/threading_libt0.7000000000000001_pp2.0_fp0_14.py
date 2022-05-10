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
