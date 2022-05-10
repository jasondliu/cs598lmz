import threading
threading.stack_size(2**27)
import sys
sys.setrecursionlimit(10**7)
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

def main():
    mod = 10**9 + 7
    N = int(input())
    a = list(map(int, input().split()))
    q = int(input())
    for _ in range(q):
        x, y = map(int, input().split())
        l = x - 1
        r = y - 1
        s = []
        for i in range(l, r + 1):
            s.append(a[i])
        s.sort()
        for i in range(l, r + 1):
            a[i] = s[i - l]
        x = 0
        for i in range(len(a)):
            x += a[i] * i
        x %= mod
        print(x)

threading.Thread(target=main).start()
