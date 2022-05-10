import threading
threading.stack_size(2**27)
import sys
sys.setrecursionlimit(10**7)
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

def main():
    n = int(input())
    a = list(map(int, input().split()))
    s = set(a)
    if len(s) == 1:
        print(n // 2)
        return
    m = min(s)
    M = max(s)
    if m == M:
        print(n // 2)
        return
    if n % 2 == 0:
        if a[0] == a[-1]:
            print(n // 2 - 1)
            return
        else:
            print(n // 2)
            return
    else:
        if a[0] == a[-1]:
            print(n // 2)
            return
        else:
            print(n // 2 + 1)
            return


threading.Thread(target=main).start()
