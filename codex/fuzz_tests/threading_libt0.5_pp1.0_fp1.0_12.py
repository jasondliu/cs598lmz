import threading
threading.stack_size(2**27)
import sys
import math
sys.setrecursionlimit(10**7)
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

n = int(input())

def rec(arr, i):
    if i == n:
        print(*arr)
        return
    for j in range(i + 1, n + 1):
        arr.append(j)
        rec(arr, j)
        arr.pop()

rec([], 0)
