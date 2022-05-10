import threading
threading.stack_size(2**30)
sys.setrecursionlimit(10**9)
from collections import defaultdict

from heapq import heappop, heappush

def dijkstra(s, e, G, N):
    INF = float("inf")
    dist = [INF] * N
    dist[s] = 0
    seen = [False] * N
    prev = [None] * N

    while True:
        cur = -1
        cur_dist = INF
        for n in range(N):
            if not seen[n] and dist[n] < cur_dist:
                cur_dist = dist[n]
                cur = n
        if cur == -1:
            break
        seen[cur] = True
        for next_, cost in G[cur]:
            if dist[next_] > dist[cur] + cost:
                dist[next_] = dist[cur] + cost
                prev[next_] = cur
    return dist[e], prev

def main():
    N, M = map(int, input().
