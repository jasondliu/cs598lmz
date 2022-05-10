import threading
threading.stack_size(2**27)
import sys
sys.setrecursionlimit(10**7)
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
def takeInput():
    return [int(x) for x in input().strip().split()]
 
 
def calculate(n, k):
    if n == 0:
        return 0
    if n == 1:
        return k
    same = calculate(n - 1, k)
    diff = calculate(n - 1, k - 1)
    return same + diff * (k - 1)
 
 
def solve():
    t = int(input())
    while t > 0:
        n, k = takeInput()
        print(calculate(n, k))
        t -= 1
 
 
if __name__ == '__main__':
    solve()
