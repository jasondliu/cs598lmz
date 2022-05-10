import sys, threading
threading.Thread(target=lambda: sys.stdin.readline()).start()

def main():
    n = int(input())
    res = 1
    for i in range(2, n + 1):
        res += i * (i - 1)
    print(res)

