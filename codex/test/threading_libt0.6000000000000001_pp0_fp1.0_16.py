import threading
threading.stack_size(2**27)
import sys

sys.setrecursionlimit(10**7)
sys.stdin = open('inpy.txt', 'r')
sys.stdout = open('outpy.txt', 'w')

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        lst = list(map(int, input().split()))
        lst.sort()
        print(lst[-1] + lst[-2])
main()
