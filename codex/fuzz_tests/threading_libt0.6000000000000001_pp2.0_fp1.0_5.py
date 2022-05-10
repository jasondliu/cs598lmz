import threading
threading.stack_size(2**27)  # Increase stack size to prevent MemoryError
import sys
sys.setrecursionlimit(10**7)  # Increase recursion limit to prevent StackOverflowError

def solve():
    n, m = map(int, input().split())
    adj = {i: [] for i in range(1, n + 1)}
    for _ in range(m):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)

    # Build a lazy segment tree
    seg = [[[]] * (n + 1) for _ in range(n + 1)]
    seg[0][0] = list(range(1, n + 1))
    for i in range(1, n + 1):
        seg[i][0] = list(set(seg[i - 1][0]) - set(adj[i]))

    for i in range(1, n + 1):
        for j in range(1, n - i + 1):
            seg[i
