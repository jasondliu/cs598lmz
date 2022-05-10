import sys, threading
threading.Thread(target=lambda: sys.stdout.flush()).start()

sys.setrecursionlimit(10**6)
input = sys.stdin.readline
INF = 1e9
MOD = 1000000007

def main():
    N = int(input())
    A = list(map(int, input().split()))

    sum_a = sum(A)
    sum_l = 0

    ans = []

    for i in range(N):
        sum_l += A[i]
        sum_a -= A[i]

        ans.append(sum_l * sum_a)

    print(*ans)

if __name__ == '__main__':
    main()
