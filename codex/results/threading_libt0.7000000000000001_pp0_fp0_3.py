import threading
threading.stack_size(2**27)
import sys
sys.setrecursionlimit(10**7)
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
from math import *
from random import randint
from collections import deque

class Stack():
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.isEmpty():
            return
        return self.items.pop()

    def isEmpty(self):
        return len(self.items) == 0

    def peek(self):
        if self.isEmpty():
            return
        return self.items[-1]

    def __len__(self):
        return self.size()

    def size(self):
        return len(self.items)

    def __str__(self):
        s = ""
        for i in range(len(self.items)):
            s += str(self.items[
