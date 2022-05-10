import sys, threading
threading.Thread(target=lambda: sys.stdout.write("\x1b[200~\n"), daemon=True).start()

import inspect, math, os, pickle, shutil, time, random, operator
from collections import defaultdict, namedtuple, Counter, deque
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
from itertools import combinations, chain, permutations
from functools import reduce
from heapq import heappush, heappop, nlargest, nsmallest
from bisect import bisect_left, bisect_right
from math import ceil, floor, factorial, gcd, modf, log, log2, log10, sqrt, lcm, acos, asin, atan, atan2, cos, sin, tan, acosh, asinh, atanh, cosh, sinh, tanh, exp, lgamma
from fractions import Fraction
from string import ascii_lowercase, ascii_uppercase, digits, hexdigits, octdigits
from operator import attrgetter, itemgetter, methodcaller
from
