import threading
threading.stack_size(2**27)
import sys
sys.setrecursionlimit(10**7)
sys.stdin = open('inpy.txt', 'r')
sys.stdout = open('outpy.txt', 'w')
from math import *
from collections import deque, Counter
from collections import defaultdict
from heapq import heappush, heappop

# mod가 있는 정수를 받으면, 숫자가 클 경우 mod를 뺀 나머지를 반환해주는 함수
def mod_positive(n, mod):
    return n % mod + (n < 0) * mod

# 좌표를 받으면, 그 좌표에 해당하는 칸의 상
