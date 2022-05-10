import sys, threading

def run():
    sys.stdin = open('SWEA\\1953\\input.txt')
    for _ in range(int(input())):
        N, M, R, C, L = map(int, input().split())
        Map = [list(map(int, input().split())) for _ in range(N)]
        Dis = [N * [1e9] for _ in range(M)]

        Q = []
        Dis[R][C] = 0

        Visited = [[False] * M for _ in range(N)]
        Visited[R][C] = True

        Cur = [0, 0, R, C]
        Cur[0] = [Cur[2] + i[0] for i in [[1, 0], [-1, 0], [0, 1], [0, -1]] if Cur[2] + i[0] >= 0 and Cur[2] + i[0] < N and Cur[3] + i[1] >= 0 and Cur[3] + i[1] < M and Map[Cur[2] + i[0]][Cur[3]
