import sys, threading
threading.Thread(target=lambda: sys.stdin.read(), daemon=True).start()

while 1:
    n, k = map(int, input().split())
    print(n**k)
