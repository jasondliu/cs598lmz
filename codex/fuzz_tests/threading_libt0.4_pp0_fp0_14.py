import threading
threading.stack_size(2**27)
import sys
sys.setrecursionlimit(10**7)
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
from math import *
from collections import *
from queue import Queue
from heapq import *
from time import gmtime, strftime
import re
#import networkx as nx

def inp(): return int(sys.stdin.readline())
def inp_list(): return list(map(int, sys.stdin.readline().split()))

def dijkstra(graph, start, end):
    # graph = {'a': {'b': 10, 'c': 3},
    #          'b': {'c': 1, 'd': 2},
    #          'c': {'b': 4, 'd': 8, 'e': 2},
    #          'd': {'e': 7},
    #          'e': {'d': 9}}
    # start = 'a'
    # end = 'e
