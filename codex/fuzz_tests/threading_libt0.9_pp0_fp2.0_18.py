import threading
threading.stack_size(2**27)
import sys
sys.setrecursionlimit(10**7)
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from collections import defaultdict, deque
from copy import deepcopy
import heapq
from itertools import combinations, permutations
from itertools import combinations_with_replacement
from functools import lru_cache
from bisect import bisect_left, bisect_right
input = sys.stdin.readline

"""
Code starts from here
"""
def dijkstra(s, dist, weight, nodes):

    dist = defaultdict(dict)
    pq = []
