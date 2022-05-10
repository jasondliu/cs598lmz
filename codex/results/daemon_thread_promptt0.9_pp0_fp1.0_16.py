import threading
# Test threading daemon (Need read more)
import queue
# Test Queue
import operator
from functools import reduce
# Test reduce
import datetime
from bisect import insort_left, bisect_left
# Test bisect
from timeit import Timer
# Test timeit

from pylzma import *
from chapter15 import *
from utils import *

# -------------------------------
# Test chapter 7 .
# -------------------------------

# Test argparse.
def TestArgumentParse():
    baseParser = argparse.ArgumentParser(add_help=False)
    baseParser.add_argument('--plot', action='store_true', default=False,
                            help='Plot the most appearing words')
    baseParser.add_argument('--bar', action='store_true', default=False,
                            help='Bar the most appearing words')
    baseParser.add_argument('--limit', '-l', nargs='?', type=int, default=None,
                            const=10, help='Limit word count')
    baseParser.add_argument('--verbose', '-v',
