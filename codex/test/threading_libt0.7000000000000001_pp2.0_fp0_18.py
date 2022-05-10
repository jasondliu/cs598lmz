import threading
threading.stack_size(2**27)
import sys
sys.setrecursionlimit(10**7)
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def S(): return input()
def HI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))
def LI_(): return [int(x)-1 for x in input().split()]
def LF(): return list(map(float, input().split()))
def LS(): return input().split()
def PI(n): return [I() for i in range(n)]
def PLF(n): return [LI() for i in range(n)]
def PLI(n): return [LI() for i in range(n)]
def PLIF(n): return [LIF() for i in range(n)]
def PLS(n): return [LS() for i in range(n)]
