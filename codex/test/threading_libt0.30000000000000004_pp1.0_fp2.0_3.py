import threading
threading.stack_size(2**27)
import sys
sys.setrecursionlimit(10**7)
sys.stdin = open('inpy.txt', 'r')
sys.stdout = open('outpy.txt', 'w')
from math import *
from collections import *
from queue import PriorityQueue
from heapq import heapify, heappop, heappush

#initialize
def initialize():
    pass

#class
class Solution:
    def __init__(self):
        self.ans = 0
    def solution(self):
        self.ans = 0
        return self.ans

def solve(tc):
    S = Solution()
    S.solution()
    print('Case #%d: %s' % (tc, S.ans))

if __name__ == '__main__':
    for tc in range(1, int(input()) + 1):
        solve(tc)
