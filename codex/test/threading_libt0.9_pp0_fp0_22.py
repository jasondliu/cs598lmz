import threading
threading.stack_size(2**27)
import sys
sys.setrecursionlimit(10**7)
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
def takeInput():
    return [int(x) for x in input().strip().split()]


def maxNum(n, m, lst):
    left = [[0 for x in range(m)]for y in range(n)]
    
    # Filling first column of left
    for i in range(n):
        left[i][0] = lst[i][0]
    # Filling first row of left
    for j in range(1, m):
        left[0][j] = lst[0][j]
    
    for i in range(1, n):
        for j in range(1, m):
            left[i][j] = max(left[i-1][j]+lst[i][j], left[i][j-1]+lst[i][j])

    
    # Print left 2
