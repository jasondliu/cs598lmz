import sys, threading
threading.Thread(target=lambda: sys.stdout.write(input())).start()

a, b, c = [int(input()) for _ in range(3)]
if a == b:
    print(c)
elif b == c:
    print(a)
else:
    print(b)
