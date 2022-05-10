import threading
threading.stack_size(2**27)
import sys
sys.setrecursionlimit(10**9)
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
from queue import Queue
from collections import deque
from collections import Counter
from copy import deepcopy
from math import log, pow, sqrt, floor, ceil
from fractions import *
from time import time
def print(*args, **kwargs):
    for x in args:
        print(x, end =" ")
    print()
    return
#------------------------- END OF TEMPLATE ---------------------------#

def main():
    testcases = int(input())
    for testcase in range(testcases):   
        n = int(input())
        stack = [int(x) for x in input().split()]
        stack.reverse()
        stack = deque(stack)
        k = int(input())
        for i in range(k + 1, n+1):
            if stack[0] < stack[i]:
                stack
