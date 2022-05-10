import threading
threading.stack_size(2**27)
import sys
sys.setrecursionlimit(10**7)
sys.stdin = open('inpy.txt', 'r')
sys.stdout = open('outpy.txt', 'w')
from math import *
from collections import *
from queue import PriorityQueue
from heapq import heappush, heappop

mod = 10 ** 9 + 7
inf = float('inf')
ninf = -float('inf')

# ---------------------------------------------------------#
# sys.stdin = open('input.txt', 'r')
# sys.stdout = open('output.txt', 'w')
# ---------------------------------------------------------#

def takeInput():
    return [int(x) for x in input().strip().split()]


def printList(arr, n):
    for i in range(n):
        print(arr[i], end=" ")
    print()


def check(arr, n):
    for i in range(n):
        if arr[i] == 0:
            return False
    return True


def solve():

