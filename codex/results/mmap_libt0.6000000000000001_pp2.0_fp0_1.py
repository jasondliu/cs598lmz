import mmap
from itertools import count, izip
from collections import defaultdict
from collections import Counter
from collections import OrderedDict
from collections import namedtuple
from collections import deque
from heapq import heappush, heappop
from bisect import bisect_left, bisect_right, insort_left, insort_right
from operator import itemgetter, attrgetter
from copy import deepcopy
from operator import add, mul, xor
from functools import wraps, partial
from fractions import Fraction
from string import maketrans, translate
from io import open

def get_input(FILE): return open(FILE).readline().strip()
def get_ints(s): return map(int, re.findall(r'\d+', s))
def gets(s): return re.findall(r'\w+', s)

def debug(*args):
    print >> sys.stderr, 'DEBUG', ' '.join(map(str, args))

#---------------------------------------------

def solve(s):
    if s == '0':
        return
