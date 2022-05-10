import gc, weakref
from itertools import *
from functools import *
import operator
import heapq
import sys
import threading
from sys import argv

N = int(argv[1])

class Thread(threading.Thread):
    def run(self):
        global v
        v = dict((i, 0) for i in xrange(N))
        for i in xrange(N):
            v[i] = i

t = Thread()
t.start()
t.join()

gc.collect()
sys.exit(0)
