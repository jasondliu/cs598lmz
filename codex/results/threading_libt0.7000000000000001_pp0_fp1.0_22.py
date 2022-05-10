import threading
threading.stack_size(2**27)
import sys
sys.setrecursionlimit(10**7)
sys.stdin = open('inpy.txt', 'r')
sys.stdout = open('outpy.txt', 'w')
from math import *
from fractions import *
from decimal import *
from itertools import *
from pair import *
from collections import *
from queue import *
from heapq import *
from itertools import *
from operator import *
ans = []
def main():
    s = input()
    a = input()
    ans.append(a)
    for i in range(min(len(s), len(a))):
        if s[i] == a[i]:
            ans.append(a[i])
        else:
            break
    print(''.join(ans))
main()
