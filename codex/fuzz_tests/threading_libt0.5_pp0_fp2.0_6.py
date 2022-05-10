import threading
threading.stack_size(2**27)
import sys
sys.setrecursionlimit(10**7)
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

def main():
    n, m, k = map(int, input().split())
    a = [0]
    a += list(map(int, input().split()))
    b = [0]
    b += list(map(int, input().split()))
    for i in range(1, n + 1):
        a[i] += a[i - 1]
    for i in range(1, m + 1):
        b[i] += b[i - 1]
    ans = 0
    j = m
    for i in range(n + 1):
        if a[i] > k:
            break
        while b[j] > k - a[i]:
            j -= 1
        ans = max(ans, i + j)
    print(ans)

threading.Thread(target=main).start()
