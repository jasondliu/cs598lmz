import threading
threading.stack_size(2**27)
import sys
sys.setrecursionlimit(10**7)
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
from math import *
from collections import deque
from collections import Counter
from collections import defaultdict
from heapq import heappush, heappop, heapify
from bisect import bisect_left, bisect, bisect_right
from itertools import permutations
from itertools import combinations
from itertools import accumulate
from functools import reduce
from copy import deepcopy
from fractions import Fraction
from string import ascii_lowercase, ascii_uppercase, digits
from bisect import bisect_left, bisect_right
from fractions import gcd
from random import randint


def LIS(nums):
    n = len(nums)
    dp = [1] * n
