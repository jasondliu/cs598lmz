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
#import re
#import networkx as nx
#import urllib.request
#from scipy.sparse import csr_matrix
#from scipy.sparse.csgraph import shortest_path, dijkstra, floyd_warshall, bellman_ford, johnson
#from scipy.sparse.csgraph import connected_components
#from scipy.sparse import csgraph
#import sklearn
def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x)-1 for x in sys.stdin.readline().split()]
