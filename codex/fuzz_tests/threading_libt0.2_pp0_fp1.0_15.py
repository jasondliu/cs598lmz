import threading
threading.stack_size(2**27)
import sys
sys.setrecursionlimit(10**7)
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
from math import *
from collections import *
from queue import Queue
from heapq import heappush, heappop, heapify
 
my_file = open("input.txt", "r")
input = my_file.read().split("\n")
 
n = int(input[0])
a = list(map(int, input[1].split()))
 
def solve(n, a):
    ans = 0
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if a[i] + a[j] > a[k] and a[j] + a[k] > a[i] and a[k] + a[i] > a[j]:
                    ans += 1
    return ans
 
print(solve
