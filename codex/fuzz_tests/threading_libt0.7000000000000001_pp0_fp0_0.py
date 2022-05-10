import threading
threading.stack_size(2**27)
import sys
sys.setrecursionlimit(10**7)
sys.stdin = open('inpy.txt', 'r')
sys.stdout = open('outpy.txt', 'w')
from math import *
from collections import defaultdict, deque
from queue import Queue
from copy import deepcopy
from time import sleep
from heapq import heappush as hp, heappop as hpop, heapify
#from collections import deque
"""
#double ended queue
d = deque()
d.append(5)
d.appendleft(10)
d.clear()
print(d)
"""

"""
# heap queue
heap = []
heappush(heap, 5)
print(heappop(heap))
heapify(heap)
heap = [5, 7, 9, 1, 3]
heapify(heap)
print(heap)
"""
def inin():
    f = open('input.txt')
    #return raw_input()
    return f.readline
