import threading
threading.stack_size(2**27)
import sys
sys.setrecursionlimit(10**7)
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
def I(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LMI(): return list(map(int, sys.stdin.readline().split()))
MOD = 10 ** 9 + 7
INF = float('inf')

N = I()
A = LMI()

# 各要素の個数を数える
cnt = Counter(A)
# 各要素の個数が1個のものをリストにする
one_list = [k for k, v in cnt.items() if v == 1]
# 各要素の個数が2個のものをリストにする
