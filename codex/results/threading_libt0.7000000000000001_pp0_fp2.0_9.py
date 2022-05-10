import threading
threading.stack_size(2**27)
import sys
sys.setrecursionlimit(10**7)
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

def main():
    a, b = map(int, input().split())
    if a > b:
        a, b = b, a
    print(min(abs(a - b), 10 - abs(a - b)))


main()
