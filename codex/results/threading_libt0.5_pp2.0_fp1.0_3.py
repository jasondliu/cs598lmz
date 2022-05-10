import threading
threading.stack_size(2**27)
import sys
sys.setrecursionlimit(10**7)
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

n = int(input())
a = list(map(int, input().split()))
cnt = 0

while True:
    if 0 in a:
        break
    for i in range(n):
        if a[i] % 2 != 0:
            break
        else:
            a[i] //= 2
    cnt += 1

print(cnt)
