import threading
threading.stack_size(2**27)
import sys
sys.setrecursionlimit(10**7)
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

def main():
    n = int(input())
    a = [[int(c) for c in input()] for i in range(n)]
    b = [[int(c) for c in input()] for i in range(n)]
    deg = [[0]*n for i in range(n)]
    for i in range(n):
        for j in range(n):
            if a[i][j] == 1: deg[i][j] += 1
            if b[i][j] == 1: deg[i][j] += 1
            if a[i][j] == 1 and b[i][j] == 1: deg[i][j] -= 1
    for i in range(n):
        for j in range(n):
            if deg[i][j] == 0:
                print('NO')
                return
   
