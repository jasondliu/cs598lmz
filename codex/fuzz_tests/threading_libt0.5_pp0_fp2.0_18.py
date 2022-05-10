import threading
threading.stack_size(2**27)
import sys
sys.setrecursionlimit(10**7)
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

def main():
    n = int(input())
    for i in range(n):
        l = list(map(int, input().split()))
        s = l[0]
        c = l[1]
        k = l[2]
        t = s
        for i in range(c):
            t = t * k
            if t > 1000000000:
                print('ALARM')
                break
        if t < 1000000000:
            print(t)

main()
