import threading
threading.stack_size(2**27)
import sys
sys.setrecursionlimit(10**7)
sys.stdin = open('inpy.txt', 'r')
sys.stdout = open('outpy.txt', 'w')
from sys import *
import bisect
from math import *
from heapq import *
from collections import *
from queue import PriorityQueue
from itertools import *
from functools import *
from operator import *
from time import *
sys.setrecursionlimit(10 ** 9)
inf = 9999999999999999999999999999999999999999999999999999
mod = 1000000007
# default import
from collections import defaultdict, Counter, deque
from operator import itemgetter
from itertools import product, permutations, combinations
from bisect import bisect_left, bisect_right, insort_left, insort_right
from math import gcd, floor, ceil

for _ in range(int(input())):
    n, m, k = map(int, input().split())
