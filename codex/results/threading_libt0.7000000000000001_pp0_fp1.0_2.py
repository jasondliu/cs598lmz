import threading
threading.stack_size(2**27)
import sys

sys.setrecursionlimit(10**7)

def qread(typ=int):
    return list(map(typ,input().split()))

def solve(A,B,C):
    A,B,C = sorted([A,B,C])

    if A+B<C:
        return 0

    if A!=B and B!=C and A!=C:
        return 1

    if A==B:
        if A==C:
            return -1
        else:
            return 3
    else:
        return 2


def main():
    T = int(input())
    for _ in range(T):
        A,B,C = qread()
        print(solve(A,B,C))

main()
