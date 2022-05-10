import threading
threading.stack_size(2**27)
import sys
sys.setrecursionlimit(10**7)
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

n = int(input())
a = [int(i) for i in input().split()]

def find(x):
    if x == a[x]:
        return x
    else:
        a[x] = find(a[x])
        return a[x]

def union(x, y):
    a[find(x)] = find(y)

for i in range(n):
    union(i, a[i])

for i in range(n):
    print(find(i) + 1, end=' ')
