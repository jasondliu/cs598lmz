import sys, threading

def run():
    sys.stdin = open('input.txt')
    read = sys.stdin.readline

    a, b, c, d = map(int, read().split())
    if (a + b + c) == d and (b + c + d) == a and (c + d + a) == b and (d + a + b) == c:
        print('YES')
    else:
        print('NO')

t = threading.Thread(target=run)
t.start()
