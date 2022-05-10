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
