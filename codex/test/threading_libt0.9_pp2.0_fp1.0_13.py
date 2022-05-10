import threading
threading.stack_size(2**27)
import sys
sys.setrecursionlimit(10**9)
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

seg = [[0 for j in range(4*Nmax)] for i in range(4*Nmax)]

def build(x, y, v, tl, tr) :
    if tl == tr :
        seg[v][y] = a[x][tl]
        return
    tm = (tl + tr) // 2
    build(x, 2*y, v, tl, tm)
    build(x, 2*y+1, v, tm+1, tr)
    seg[v][y] = seg[v][2*y] + seg[v][2*y+1]

def build(y, v, tl, tr) :
    if tl == tr :
        build(tl, v, 1, 0, n-1)
        return
