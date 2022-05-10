import threading
threading.stack_size(2**27)
import sys
sys.setrecursionlimit(10**7)
sys.stdin = open('inpy.txt', 'r')
sys.stdout = open('outpy.txt', 'w')
from math import floor, sqrt, log
from collections import Counter, deque
from fractions import Fraction
from decimal import Decimal
from time import time
# from functools import lru_cache, cmp_to_key
# from functools import cmp_to_key
# print = lambda *a, **k: print(*a, file=sys.stderr, **k)

# show_flg = True
show_flg = False


def print_result(case: int, **kwargs):
    if show_flg:
        s = 'Case #{}: '.format(case)
        if '1' in kwargs: s += str(kwargs['1']) + ' '
        if '2' in kwargs: s += str(kwargs['2']) + ' '
