import threading
threading.stack_size(2**27)
import sys
sys.setrecursionlimit(10**7)
sys.stdin = open('inpy.txt', 'r')
sys.stdout = open('outpy.txt', 'w')
from math import *
from collections import *
from queue import Queue
from heapq import *
from time import sleep
from random import *
import bisect
from bisect import *


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


def cal_sieve(n):
    prime = [True for i in range(n + 1)]
    p = 2
    while (p * p <= n):

        # If prime[p] is
