import threading
threading.stack_size(2**27)
import sys
sys.setrecursionlimit(10**7)
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

def main():
    t = int(input())
    while t > 0:
        n = int(input())
        a = [int(x) for x in input().split()]
        b = [int(x) for x in input().split()]
        a.sort()
        b.sort()
        s = 0
        for i in range(n):
            s += min(a[i], b[i])
        print(s)
        t -= 1


threading.Thread(target=main).start()
