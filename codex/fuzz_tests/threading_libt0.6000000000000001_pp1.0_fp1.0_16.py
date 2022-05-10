import threading
threading.stack_size(2**27)
import sys
sys.setrecursionlimit(10**7)
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

from math import inf, sqrt
from heapq import heappush, heappop, heapify
 
def ip(): return int(sys.stdin.readline())
def sip(): return sys.stdin.readline()
def mip(): return map(int, sys.stdin.readline().split())
def mips(): return map(str, sys.stdin.readline().split())

def lcm(a,b): return abs(a*b) // math.gcd(a,b)
def gcd(a,b): return math.gcd(a,b)

def factors(n): # find the factors of a number
    return list(set(reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0
