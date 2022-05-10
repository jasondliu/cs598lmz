import threading
threading.stack_size(2**27)
import sys
sys.setrecursionlimit(10**7)
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

mod = 10**9 + 7

def pow(x, y, m):
    if y == 0:
        return 1
    elif y % 2 == 0:
        return pow(x, y // 2, m) * pow(x, y // 2, m) % m
    else:
        return x * pow(x, y - 1, m) % m

def inv(x, m):
    return pow(x, m - 2, m)

def fact(n, m):
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i % m
    return fact

def invfact(n, m):
    return inv(fact(n, m), m)

def nCr(n, r, m):
    return fact(n, m) * invfact(r, m
