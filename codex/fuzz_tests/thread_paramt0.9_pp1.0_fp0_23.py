import sys, threading
threading.Thread(target=lambda: sys.stdin.readline()).start()
'''

if __name__ == '__main__':
    n = int(input())
    arr = [int(x) for x in input().split()]
    print(' '.join(map(str, arr[::-1])))
