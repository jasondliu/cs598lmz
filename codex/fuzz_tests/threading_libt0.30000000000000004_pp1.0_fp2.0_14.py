import threading
threading.stack_size(2**27)
import sys
sys.setrecursionlimit(10**7)
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

def main():
    n = int(input())
    a = list(map(int, input().split()))
    dp = [0] * n
    dp[0] = a[0]
    dp[1] = max(a[0], a[1])
    for i in range(2, n):
        dp[i] = max(dp[i-1], dp[i-2] + a[i])
    print(dp[-1])

threading.Thread(target=main).start()
