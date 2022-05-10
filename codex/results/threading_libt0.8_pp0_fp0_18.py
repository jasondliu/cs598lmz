import threading
threading.stack_size(2**27)
import sys
sys.setrecursionlimit(10**7)
sys.stdin = open('inpy.txt', 'r')
sys.stdout = open('outpy.txt', 'w')
import queue
from collections import deque,defaultdict
from collections import OrderedDict
from math import sqrt, log, log2
from fractions import Fraction
from decimal import Decimal, getcontext
from time import time
from bisect import bisect_left as bl, bisect_right as br, insort_left as il, insort_right as ir
from itertools import permutations, combinations, product, accumulate, cycle
from operator import itemgetter, mul, xor, add, substract
from copy import deepcopy
from functools import reduce
from string import ascii_lowercase, ascii_uppercase, digits
from fractions import gcd
from math import floor, ceil
mod = 10 ** 9 + 7
inf = float('inf')
ninf = -float('inf')
 
# ---------------------------------------------------------#
# sys.
