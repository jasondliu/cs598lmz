import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\x1b[2J\x1b[H')).start()

import itertools
from collections import Counter
from functools import reduce
from operator import mul
from functools import reduce
from fractions import Fraction
from math import sqrt, atan2, cos, sin, pi, log, log10, floor, ceil
from random import randint, shuffle
from copy import deepcopy
from time import time

T = int(input())
for test in range(T):
    N, J = map(int, input().split())
    print('Case #{}:'.format(test+1))
    coins = set()
    while len(coins) < J:
        coin = [1]
        
        while True:
            start = 0
            end = N - 1
            mid = (start + end) // 2
            x = randint(start, mid)
            y = randint(x + 1, end)
            
            coin.append(x)
            coin.append(y)
            
            if x == y:

