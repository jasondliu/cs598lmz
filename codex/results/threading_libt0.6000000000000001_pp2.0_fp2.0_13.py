import threading
threading.stack_size(2**27)
import sys
import copy
sys.setrecursionlimit(10**7)

def main():
    def warshall_floyd(d):
        # d[i][j]: iからjへの最短距離
        for k in range(N):
            for i in range(N):
                for j in range(N):
                    d[i][j] = min(d[i][j], d[i][k] + d[k][j])
        return d

    N, M, R = LI()
    r = LI()
    r = [r[i] - 1 for i in range(R)]
    d = [[10**18 for i in range(N)] for j in range(N)]
    for i in range(N):
        d[i][i] = 0

    for _ in range(M):
        a, b, c = LI()
        a -= 1
        b -= 1
        d[a][b] = c
        d[b][a] = c
