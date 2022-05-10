import threading
threading.stack_size(2**27)
import sys
sys.setrecursionlimit(10**7)
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
def takeInput():
    return [int(x) for x in input().strip().split()]
def printList(arr, n, sep=' '):
    for i in range(n):
        print(arr[i], end=sep)
    print()
def modInv(a, m):
    g = gcdExtended(a, m)
    return a//g[0]
def gcdExtended(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = gcdExtended(b%a, a)
    x = y1 - (b//a) * x1
    y = x1
    return gcd, x, y
def gcd(a, b):
    if(a==0):
        return b 
    return gcd(b%
