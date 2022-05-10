import threading
threading.stack_size(2**27)
import sys
sys.setrecursionlimit(10**7)
sys.stdin = open('inpy.txt', 'r')
sys.stdout = open('outpy.txt', 'w')
from math import *
from collections import defaultdict
from collections import deque
from queue import Queue
from heapq import heappush, heappop, heapify
import math
from itertools import permutations, combinations
from itertools import accumulate, product, combinations_with_replacement
from bisect import bisect_left, bisect_right
from copy import deepcopy
from operator import itemgetter
from functools import reduce
from string import ascii_uppercase, ascii_lowercase
from fractions import gcd
import time
def lcm(a, b):
    return (a * b) // gcd(a, b)
sys.setrecursionlimit(10 ** 6)
#import queue
#from collections import deque
#from threading import Thread
#import time
#import sys
#import io
#import at
