import threading
threading.stack_size(2**27)
import sys
sys.setrecursionlimit(10**9)
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

mod = 998244353

def dfs(graph,start,visited):
    visited[start] = True
    for i in graph[start]:
        if not visited[i]:
            dfs(graph,i,visited)

def main():
    n, m = map(int,input().split())
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b = map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)
    visited = [False] * (n+1)
    count = 0
    for i in range(1,n+1):
        if not visited[i]:
            dfs(graph,i,visited)
            count += 1
    print(count - 1)


