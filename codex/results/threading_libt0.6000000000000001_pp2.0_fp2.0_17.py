import threading
threading.stack_size(2**27)
import multiprocessing
sys.setrecursionlimit(10**7)
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

def main():
    n, m = map(int, input().split())

    a = [int(i) for i in input().split()]
    b = [int(i) for i in input().split()]

    c = [0]*(n+1)
    for i in range(n):
        c[i] = a[i] - b[i]

    c.sort()

    # print(c)
    count = 0
    for i in range(n):
        if c[i] > 0:
            break
        else:
            count += 1
    # print(count)
    sum = 0
    for i in range(n-1, -1, -1):
        if sum < 0:
            break
        else:
            sum += c[i]
    # print(n-
