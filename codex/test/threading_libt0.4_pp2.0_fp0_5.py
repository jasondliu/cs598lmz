import threading
threading.stack_size(2**27)
import sys
sys.setrecursionlimit(10**7)
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

n, m = map(int, input().split())
a = [list(map(int, input().split())) for i in range(n)]

def check(x, y):
    for i in range(n):
        for j in range(m):
            if a[i][j] > a[x][y]:
                return False
    return True

def check2(x, y):
    for i in range(n):
        for j in range(m):
            if a[i][j] < a[x][y]:
                return False
    return True

for i in range(n):
    for j in range(m):
        if not check(i, j):
            print(-1)
            exit()

ans = 0
