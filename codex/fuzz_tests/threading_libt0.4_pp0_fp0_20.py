import threading
threading.stack_size(2**27)
import sys
sys.setrecursionlimit(10**7)
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
from math import *
from queue import PriorityQueue

mod = 10 ** 9 + 7
n = int(input())
a = list(map(int, input().split()))

def get_divisors(n):
    divisors = []
    for i in range(1, int(sqrt(n) + 1)):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)
    return divisors

def solve(n, a):
    ans = 0
    for i in range(n):
        divisors = get_divisors(a[i])
        for j in divisors:
            if a[i] % j == 0:
                ans += 1
    return ans

print(solve(
