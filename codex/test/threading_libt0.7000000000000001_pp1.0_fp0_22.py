import threading
threading.stack_size(2**27)
import sys

sys.setrecursionlimit(10**7)
sys.stdin = open('inpy.txt', 'r')
sys.stdout = open('outpy.txt', 'w')

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        k = int(input())
        print(subarray(arr, k))

def subarray(arr, k):
    max_len = 0
    max_sub = 0
    curr_sub = 0
    curr_len = 0
    for i in range(len(arr)):
        curr_sub += arr[i]
        curr_len += 1
        if curr_sub > k:
            if curr_len > max_len:
                max_len = curr_len
                max_sub = curr_sub
            curr_sub = 0
            curr_len = 0
