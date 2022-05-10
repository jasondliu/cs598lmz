import threading
threading.stack_size(2**27)
import sys
sys.setrecursionlimit(10**7)
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

n, m = map(int, input().split())

# n - кол-во ребер
# m - кол-во вершин

a = [[] for _ in range(m)]

for i in range(n):
    x, y, w = map(int, input().split())
    a[x - 1].append((y - 1, w))


def dfs(v, p=-1):
    if not a[v]:
        return

    for u, w in a[v]:
        if u == p:
            continue
        dfs(u, v)
        a[v][a[v].index((u, w))] = (u, min(w, a[u][0][1]))


dfs(0)

