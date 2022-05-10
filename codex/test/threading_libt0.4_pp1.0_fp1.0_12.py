import threading
threading.stack_size(2**27)
import sys
sys.setrecursionlimit(10**7)
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
from math import *
from collections import defaultdict, deque
from collections import Counter, OrderedDict
from fractions import gcd
from random import randint
from time import time
from itertools import product
from operator import itemgetter
from functools import reduce
from bisect import bisect_left, bisect_right
from heapq import heappop, heappush
from string import ascii_lowercase
from copy import deepcopy
from io import BytesIO, IOBase

mod = 1000000007

# FastIO Region
BUFSIZE = 8192
class FastIO(IOBase):
    newlines = 0
    def __init__(self, file):
        self._fd = file.fileno()
        self.buffer = BytesIO()
