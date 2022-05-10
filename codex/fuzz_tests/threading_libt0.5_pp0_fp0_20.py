import threading
threading.stack_size(2**27)
import sys
sys.setrecursionlimit(10**7)
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

def main():
    n = int(input())
    arr = [0]*n
    for i in range(n):
        arr[i] = int(input())
    arr.sort()
    print(arr[n//2])

threading.Thread(target=main).start()
