import threading
threading.stack_size(2**27)
import sys
sys.setrecursionlimit(10**7)
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

n = int(input())
a = [int(i) for i in input().split()]

def merge(a, l, mid, r):
    temp = [0] * (r - l + 1)
    i = l
    j = mid + 1
    k = 0
    while i <= mid and j <= r:
        if a[i] < a[j]:
            temp[k] = a[i]
            i += 1
            k += 1
        else:
            temp[k] = a[j]
            j += 1
            k += 1
    while i <= mid:
        temp[k] = a[i]
        i += 1
        k += 1
    while j <= r:
        temp[k] = a[j]
        j += 1
        k += 1
