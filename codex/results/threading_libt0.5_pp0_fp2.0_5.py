import threading
threading.stack_size(2**27)
import sys
sys.setrecursionlimit(10**7)
sys.stdin = open('inpy.txt', 'r')
sys.stdout = open('outpy.txt', 'w')
from math import floor, sqrt, log
from collections import Counter, deque
from fractions import gcd
from sys import stdin, stdout
read = lambda: stdin.readline().strip()
write = lambda x: stdout.write(str(x) + '\n')

#----------------------------------------#
def main():
    n = int(read())
    a = list(map(int, read().split()))
    a.sort()
    i = 0
    j = n-1
    ans = 0
    while i < j:
        ans += (a[i] + a[j])**2
        i += 1
        j -= 1
    write(ans)
main()
