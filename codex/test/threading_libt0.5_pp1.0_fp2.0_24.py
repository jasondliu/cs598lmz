import threading
threading.stack_size(2**27)
import sys
sys.setrecursionlimit(10**7)
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
from math import *
from collections import *
from queue import PriorityQueue
from bisect import bisect_left, bisect_right
from itertools import *
from copy import deepcopy
from functools import reduce
import time

def main():
    for _ in range(int(input())):
        n = int(input())
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        a.sort()
        b.sort()
        ans = 0
        for i in range(n):
            ans += min(a[i], b[i])
        print(ans)

main()
