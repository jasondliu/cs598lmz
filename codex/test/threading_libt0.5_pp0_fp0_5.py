import threading
threading.stack_size(2**27)
import sys
sys.setrecursionlimit(10**7)
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
import random
import math
def main():
    t = int(input())
    for _ in range(t):
        n,k = map(int, input().split())
        arr = list(map(int, input().split()))
        arr.sort()
        i = 0
        while i < n and arr[i] <= k:
            k -= arr[i]
            i += 1
        print(i)
        
main()
