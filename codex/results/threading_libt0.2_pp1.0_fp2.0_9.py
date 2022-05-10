import threading
threading.stack_size(2**27)
import sys
sys.setrecursionlimit(10**7)
sys.stdin = open('inpy.txt', 'r')
sys.stdout = open('outpy.txt', 'w')
from math import *
from collections import defaultdict, deque
from queue import Queue
from copy import deepcopy
ints = lambda s: list(map(int, s.split()))
#import networkx as nx
#import re
#from scipy.sparse.csgraph import shortest_path, dijkstra, floyd_warshall, bellman_ford, johnson
#from scipy.sparse import csr_matrix
#from scipy.special import comb
#import itertools
#import math
#import sys
#sys.setrecursionlimit(10**9)
#inf = 10**19
#mod = 10**9 + 7
#EPS = 10**-10
#EPS = 0.0000000001
#mod = 998244353
#mod = 10**9+7
#mod =
