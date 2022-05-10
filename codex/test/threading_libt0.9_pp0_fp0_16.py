import threading
threading.stack_size(2**27)

sys.setrecursionlimit(10**7)

INF = 10**18
MOD = 10**9 + 7

def solve():
    H, W, K = map(int, input().split())
    S = [input() for i in range(H)]

    c1 = 0
    m = [[0] * W for i in range(H)]
    whites = [[0] * W for i in range(H)]
    for i in range(H):
        for j in range(W):
            if S[i][j] == '#':
                m[i][j] = 1
                if i > 0 and j > 0:
                    whites[i][j] += whites[i-1][j-1]
                if i > 0:
                    whites[i][j] += whites[i-1][j]
                if j > 0:
                    whites[i][j] += whites[i][j-1]
                whites[i][j] -= m[i][j]
                c1 += 1

