import threading
threading.stack_size(2*1024*1024)
sys.setrecursionlimit(10**7)

input = sys.stdin.readline


def inp():
    return int(input())


def inlt():
    return list(map(int, input().split()))


def insr():
    s = input()
    return list(s[:len(s) - 1])


def invr():
    return map(int, input().split())


def solve(x):
    pass


n = inp()
a = inlt()
b = [0] * n
b[0] = a[0]
for i in range(1, n):
    b[i] = a[i] + a[i - 1]

for i in range(n):
    print(b[i], end=" ")
