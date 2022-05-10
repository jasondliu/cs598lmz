import threading
threading.stack_size(2**27)
import sys
sys.setrecursionlimit(10**7)
sys.stdin = open('inpy.txt', 'r')
sys.stdout = open('outpy.txt', 'w')
from math import *
from fractions import *
from random import *
from collections import *
from queue import *
from heapq import *
from operator import *
# lines = sys.stdin.readlines()
# sys.stdin = open('inpy.txt', 'r')
# sys.stdout = open('outpy.txt', 'w')
from decimal import Decimal
import time
md=pow(10,9)+7
inf=10**20
#=========================================
def main():
    n=int(input())
    s=input()
    if n%2==1:
        print("No")
        return
    for i in range(n//2):
        if s[i]!=s[i+(n//2)]:
            print("No")
            return
    print("Yes")
#=========================================

