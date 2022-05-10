import threading
threading.stack_size(2**27)
import sys
sys.setrecursionlimit(10**7) # max depth of recursion
threading.start_new_thread(init, ())

def main():
    global t
    global c
    global r
    global max_c
    global max_r
    global row
    global col
    global grid
    global ans
    global x
    global y
    global c_
    global r_
    global k
    global s
    global f
    global d
    global p
    global q
    global o
    global m
    global e
    global start
    global end
    global dis
    global par
    global qu
    global ok
    global mat
    global edge
    global edge_
    global p_
    global q_
    global o_
    global m_
    global e_

    t = int(input())
    for case in range(1, t+1):
        c, r = map(int, input().split())
        grid = []
        for i in range(r):
           
