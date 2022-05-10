import threading
threading.stack_size(2**27)
import sys
sys.setrecursionlimit(10**7)
sys.stdin = open('inpy.txt', 'r')
sys.stdout = open('outpy.txt', 'w')
from math import *
from fractions import *
from collections import *
from input import *
from tabulate import *
from time import time
from copy import deepcopy
from random import randint, randrange, shuffle
import itertools
inf = 10**9


def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    if n % 2 == 0:
        print(a[n // 2 - 1])
    else:
        print(a[n // 2])


main()
