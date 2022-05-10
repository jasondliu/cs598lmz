import mmap
from collections import defaultdict
from itertools import count
from heapq import heappush, heappop
from heapq import heapify
from operator import itemgetter
from bisect import bisect_left, bisect_right
from math import ceil, floor

def read_int():
    return int(input())


def read_int_map():
    return map(int, input().split(' '))


def read_int_list():
    return list(map(int, input().split(' ')))


def read_s_list_loop(n):
    return [input() for _ in range(n)]


def read_int_map_list(n, m):
    return [read_int_list() for _ in range(n)]


def read_s_map_list(n, m):
    return [read_s_list() for _ in range(n)]


def read_s_list(n):
    return [input() for _ in range(n)]


