import threading
threading.stack_size(2**27)
import sys
sys.setrecursionlimit(10**7)
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

n = int(input())
a = list(map(int, input().split()))

d = {}
for i in range(n):
    if a[i] in d:
        d[a[i]] += 1
    else:
        d[a[i]] = 1

ans = 0
for key in d:
    if d[key] >= 3:
        ans += d[key] - 2
        d[key] = 2

d = sorted(d.items(), key=lambda x: x[0])

for i in range(len(d)):
    if d[i][1] == 1:
        for j in range(i+1, len(d)):
            if d[j][1] == 1:
                if d[j][0] > d[i][0]:
                    ans += 1

