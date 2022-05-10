import threading
threading.stack_size(2**27)
import sys
sys.setrecursionlimit(10**7)
sys.stdin = open('inpy.txt', 'r')
sys.stdout = open('outpy.txt', 'w')
from math import *
from fractions import *
from random import *
from decimal import *
from time import *
from string import *
from pprint import *
from timeit import default_timer as timer

def main():
    t = int(input())
    while t:
        n = int(input())
        lst = list(map(int, input().split()))
        lst.sort()
        sum = 0
        for i in range(n):
            j = i + 1
            while j < n and lst[j] <= lst[i] + 4:
                j += 1
            sum += (j - i - 1)
        print(sum)
        t -= 1


main()
