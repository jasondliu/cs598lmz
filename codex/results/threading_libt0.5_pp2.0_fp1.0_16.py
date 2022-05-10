import threading
threading.stack_size(2**27)
import sys
sys.setrecursionlimit(10**7)
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

n, m = map(int, input().split())
a = list(map(int, input().split()))

l = [0] * (n + 1)
for i in range(m):
    l[a[i]] += 1

ans = 0
for i in range(1, n + 1):
    if l[i] == 0:
        ans += 1
print(ans)
