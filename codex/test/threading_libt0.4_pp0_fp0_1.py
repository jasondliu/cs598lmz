import threading
threading.stack_size(2**27)
import sys
sys.setrecursionlimit(10**7)
sys.stdin = open('inpy.txt', 'r')
sys.stdout = open('outpy.txt', 'w')
from math import floor, sqrt, log
from collections import Counter, deque
from fractions import gcd
from sys import stdin, stdout
read = lambda: stdin.readline().strip()
write = lambda x: stdout.write(str(x))
# ---------------------------------------------------------
# sys.stdin = open('in.txt','r')
# sys.stdout = open('out.txt','w')
# ---------------------------------------------------------
def get_ints(): return map(int, read().split())
def get_ints_list(): return list(map(int, read().split()))
def get_ints_array(N): return [get_ints() for _ in range(N)]
def get_ints_2d_array(H, W): return [[int(x) for x in list(read())] for _ in range(H)]
