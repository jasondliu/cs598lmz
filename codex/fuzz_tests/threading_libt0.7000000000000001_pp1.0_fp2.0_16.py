import threading
threading.stack_size(2**27)
import sys
sys.setrecursionlimit(10**7)
sys.stdin = open('/home/puneet/Documents/Cpp Programs/input.txt', 'r')
sys.stdout = open('/home/puneet/Documents/Cpp Programs/output.txt', 'w')
from collections import Counter
def inv():
    return map(int, input().split())
def inp():
    return int(input())
def inlt():
    return list(map(int, input().split()))
def insr():
    s = input()
    return list(s[:len(s) - 1])
def numb(a, n, k):
    hash = [0] * (n + 1)
    prefix = [0] * (n + 1)
    for i in range(1, n + 1):
        hash[i] = (hash[i - 1] + a[i - 1] % k) % k
    for i in range(1, n + 1):
        prefix[i] = (prefix[
