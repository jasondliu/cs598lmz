import threading
threading.stack_size(2**27)
import sys
sys.setrecursionlimit(10**7)
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

from collections import deque
def bfs(start, end, adj):
    q = deque()
    q.append(start)
    visited = {}
    visited[start] = 0
    while q:
        v = q.popleft()
        for u in adj[v]:
            if u not in visited:
                visited[u] = visited[v] + 1
                q.append(u)
    return visited[end]


n, m = map(int, input().split())
adj = {}
for i in range(n):
    adj[i] = []
for i in range(m):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

start, end = map(int, input().split())
