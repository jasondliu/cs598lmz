import threading
threading.stack_size(2 ** 27)
import sys
sys.setrecursionlimit(10 ** 7)
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
from math import floor, sqrt, log


from decimal import *
getcontext().prec = 30

MOD = 10 ** 9 + 7

class SegmentTree:
    def __init__(self, array, func=min):
        self.n = len(array)
        self.size = 2 ** (int(log2(self.n - 1)) + 1) if self.n != 1 else 1
        self.func = func
        self.default = 0 if self.func != max else 10 ** 18
        self.data = [self.default] * (2 * self.size)
        self.process(array)

    def process(self, array):
        self.data[self.size: self.size + self.n] = array
