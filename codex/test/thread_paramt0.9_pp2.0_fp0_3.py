import sys, threading
threading.Thread(target=lambda:sys.stdin.readline()).start()
sys.setrecursionlimit(2147483647) 
MOD = 1000000007;
MAX = 50000
INF = 2000000000000000000;
rull = []
ans = [];
vis = []
def dfs(ik): 
    p = 0
    rull[ik] = 1
    for i in range(k):
        if adj[ik][i] == 1 and rull[i] == 0:
            p ^= (1 ^ dfs(i))
    return p


k, n = map(int, input().split())
for i in range(k):
	a, b = map(int, input().split())
	if a not in rull:
		rull[a] = 0
	if b not in rull:
	    rull[b] = 0
    
	adj[a][b] = 1
	adj[a][a] = 1
	adj[b][b] = 1
	adj[b][a] = 1

