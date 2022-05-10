import threading
threading.stack_size(2**27)
import sys
sys.setrecursionlimit(10**7)
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

MAX = 100005
mod = 998244353

def main():
    f = {0:1}
    for i in range(1,MAX):
        f[i] = (f[i-1]*i)%mod

    invf = {MAX-1:pow(f[MAX-1],mod-2,mod)}
    for i in range(MAX-2,-1,-1):
        invf[i] = (invf[i+1]*(i+1))%mod

    t = int(input())
    while t!=0:
        t-=1
        n,k = map(int,input().split())
        ans = 0
        for i in range(k+1):
            a = ((f[n-i]*invf[i])%mod*invf[n-2*i
