import threading
threading.stack_size(2**27)
import sys
sys.setrecursionlimit(10**7)
sys.stdin = open('inpy.txt', 'r')
sys.stdout = open('outpy.txt', 'w')
from fractions import gcd
def lcm(a, b): return a * b // gcd(a, b)
sys.setrecursionlimit(10**6)
threading.stack_size(2**26)
from fractions import gcd
import math
def main():
    t = int(input())
    while t > 0:
        n = int(input())
        arr = [i for i in range(n+1)]
        arr[1] = 0
        i = 2
        while i != int(math.sqrt(n)) + 1:
            if arr[i] != 0:
                for j in range(i*2, n+1, i):
                    arr[j] = 0
            i += 1
        count = 0
