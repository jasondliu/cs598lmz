import threading
threading.stack_size(67108864)

def dfs(G, v, visited):
    visited[v] = True
    for u in G[v]:
        if not visited[u]:
            dfs(G, u, visited)

def cc_dfs(G):
    visited = [False] * len(G)
    cc = 0
    for v in range(len(G)):
        if not visited[v]:
            dfs(G, v, visited)
            cc += 1
    return cc

def cc_bfs(G):
    Q = []
    cc = 0
    visited = [False] * len(G)
    for v in range(len(G)):
        if not visited[v]:
            Q.append(v)
            while Q:
                v = Q.pop(0)
                if not visited[v]:
                    visited[v] = True
                    Q.extend(G[v])
            cc += 1
    return cc

def cc_bfs2(G):
    Q, cc = [],
