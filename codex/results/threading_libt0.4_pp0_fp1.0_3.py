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
    d = list(map(int, input().split()))
    e = list(map(int, input().split()))
    f = list(map(int, input().split()))
    g = list(map(int, input().split()))
    h = list(map(int, input().split()))
    i = list(map(int, input().split()))

    dp = [[[0 for i in range(n + 1)] for j in range(n + 1)] for k in range(n + 1)]
    for k in range(1, n + 1):
        for j in
