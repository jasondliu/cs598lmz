import threading
threading.stack_size(268435456) # 64MB stack
sys.setrecursionlimit(2 ** 20)
debug = False

def dfs(u, f):
    # print(u, f)
    if u == f:
        return 0
    if u in dp:
        return dp[u]
    dp[u] = 1
    for v in adj[u]:
        dp[u] = max(dp[u], dfs(v, f) + 1)
    return dp[u]

def main():
    global adj, dp
    N, M = map(int, input().split())
    adj = defaultdict(list)
    for _ in range(M):
        u, v = map(int, input().split())
        adj[u].append(v)
    dp = {}
    res = 0
    for u in range(1, N + 1):
        res = max(res, dfs(u, u))
    print(res)


thread = threading.Thread(target=main)
thread.
