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

MOD = 1000000007

def inin():
    return int(input())


def stin():
    return input()


def spin():
    return map(int, stin().split())


def lin():                           #takes array as input
    return list(map(int, stin().split()))


def matrix(n):
    #matrix input
    return [list(map(int, input().split()))for i in range(n)]

################################################


def string2intlist(s):
    return list(map(int, s))


def calculate_sum(a, N):  #sum of a to N
    # Number of multiples
    m = N / a
    #
