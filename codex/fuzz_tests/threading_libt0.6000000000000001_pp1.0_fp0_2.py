import threading
threading.stack_size(2**27)
sys.setrecursionlimit(10**7)
INF = 10**20
MOD = 10**9 + 7

def num(x, y, dx, dy, t, S):
    if 0 <= x < H and 0 <= y < W:
        if S[x][y] == '#':
            return 0
        else:
            return t
    else:
        return 0

def dfs(x, y, dx, dy, t, S):
    res = 0
    if 0 <= x < H and 0 <= y < W and S[x][y] == '#':
        return 0
    res += num(x, y, dx, dy, t, S)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        res += dfs(nx, ny, dx, dy, t//4, S)
    return res

def solve():
    res = 0
    for i in range(H):
        for j in range(
