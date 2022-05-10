import sys, threading
threading.Thread(target=lambda: sys.stdin.readline()).start()

n, m, k = map(int, input().split())
a = list(map(int, input().split()))
a.sort()

h = a[n-1] - a[0]

l = 0
r = h
ans = 0
while l <= r:
    mid = (l+r)//2
    s = 0
    for i in range(1, n):
        s += min(mid//i, n-i)
    if s >= m:
        ans = mid
        r = mid-1
    else:
        l = mid+1

print(ans)
