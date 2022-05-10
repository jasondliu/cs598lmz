import threading
threading.stack_size(2**27)
import sys
sys.setrecursionlimit(10**9)
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
from math import *
from queue import PriorityQueue

MOD = 1000000007

def inp():
    return(int(input()))
def inlt():
    return(list(map(int,input().split())))
def insr():
    s = input()
    return(list(s[:len(s) - 1]))
def invr():
    return(map(int,input().split()))
def seq(n):
    return(list(map(int,list(str(n)))))

MOD = (int)(1e9)
match = [int(x) for x in input().split()]
n = match.pop(0)
match.pop(0)

def play(row,col,player):
    global match
    used = [[0 for i in range(n)] for j in range(n)]

