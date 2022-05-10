import sys, threading
threading.Thread(target=lambda: sys.stdin.readline().strip()).start()
def input(): return sys.stdin.readline().strip()
sys.setrecursionlimit(10**7)
INF = 10**20; MOD = 10**9 + 7
def I(): return int(input())
def F(): return float(input())
def S(): return input()
def LI(): return [int(x) for x in input().split()]
def LI_(): return [int(x)-1 for x in input().split()]
def LF(): return [float(x) for x in input().split()]
def LS(): return input().split()

def resolve():
    N, A = LI()

    # 分割数の最小値を求める
    # 個数が同じならば、素数の場合、1の周りの個数が最小になるので、素数を使う
    # 偶数の場合は
