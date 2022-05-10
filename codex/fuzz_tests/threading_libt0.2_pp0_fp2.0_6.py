import threading
threading.stack_size(2**27)
import sys
sys.setrecursionlimit(10**7)
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    a.sort()
    b.sort()
    c.sort()
    ans = 0
    for i in range(n):
        ans += (bisect.bisect_left(a, b[i]) * (n - bisect.bisect_right(c, b[i])))
    print(ans)

threading.Thread(target=main).start()
