import sys, threading
threading.Thread(target=lambda: sys.stdin.readline()).start()

n, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort()

ans = 0

for i in range(m):
    if a[i] < 0:
        ans -= a[i]

print(ans)
