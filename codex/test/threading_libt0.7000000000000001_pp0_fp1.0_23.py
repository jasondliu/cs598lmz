import threading
threading.stack_size(2**27)
import sys
sys.setrecursionlimit(10**7)
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
from math import *
from collections import deque
from collections import Counter
from collections import defaultdict
from bisect import bisect_left, bisect_right
from itertools import accumulate
from itertools import product
from itertools import combinations
from bisect import *
from math import gcd
from operator import itemgetter
def main():
  input = sys.stdin.readline
  input = input().strip().split(' ')
  n = int(input[0])
  k = int(input[1])
  array = []
  for i in range(n):
    input = sys.stdin.readline()
    array.append(input)
  c = Counter(array)
  c = sorted(c.items(), key=itemgetter(1), reverse=True)
  print(c[k-1][0])
thread
