import threading
threading.stack_size(2**27)
import sys
sys.setrecursionlimit(10**7)
sys.stdin = open('inpy.txt', 'r')
sys.stdout = open('outpy.txt', 'w')
from random import randint, randrange, random, choice
from copy import copy as copy


class Multiset:

    def __init__(self):
        self.n = 0
        self.s = set()

    def add(self, item):
        if item in self.s:
            self.s.remove(item)
            self.n -= 1
        else:
            self.s.add(item)
            self.n += 1

    def remove(self, item):
        if item in self.s:
            self.s.remove(item)
            self.n -= 1


def main():
    n, m = map(int, input().split())
    arr = [list(input()) for _ in range(n)]

    u = -1
    d = -1
    l = -1
