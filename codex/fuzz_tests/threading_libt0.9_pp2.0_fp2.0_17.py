import threading
threading.stack_size(2**27)

sys.setrecursionlimit(10**7)
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

n = int(input())

edges = []
for i in range(n):
    edges.append(list(map(int, input())))

used = [0] * n

def dfs(v):
    global edges, used, n
    used[v] = 1
    for u in range(n):
        if v == u:
            continue
        if edges[v][u] == 1 and used[u] == 0:
            dfs(u)


for i in range(n):
    if used[i] == 0:
        dfs(i)
        break

M = 10000

if used[M - 1] == 0:
    print('NO')
