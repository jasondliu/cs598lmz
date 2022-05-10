import threading
threading.stack_size(2**27)
import sys
sys.setrecursionlimit(10**9)
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

n = int(input())

def rec(m):
    if m == 1:
        return 0
    if m % 2 == 0:
        return 1 + rec(m // 2)
    else:
        return 1 + rec(m + 1)

print(rec(n))
