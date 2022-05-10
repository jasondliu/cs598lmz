import threading
threading.stack_size(2**27)
import sys
sys.setrecursionlimit(10**7)
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

n = int(input())
a = [int(i) for i in input().split()]

def make_set(v):
    p[v] = v
    r[v] = 0

def find_set(v):
    if v == p[v]:
        return v
    p[v] = find_set(p[v])
    return p[v]

def union(a, b):
    a = find_set(a)
    b = find_set(b)
    if a != b:
        if r[a] < r[b]:
            a, b = b, a
        p[b] = a
        if r[a] == r[b]:
            r[a] += 1

p = [None] * (n + 1)
