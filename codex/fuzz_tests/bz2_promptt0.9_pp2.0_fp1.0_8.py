import bz2
# Test BZ2Decompressor
from collections import deque
from multiprocessing import Queue, Process
from time import time, sleep, time

from numpy import load, frombuffer, dtype, array, isin, arange, where, save, hstack, savetxt, zeros, split
from itertools import izip
from argparse import ArgumentParser

from vectools import zip_array
from logsplitter import get_chunk_times
from splitter import *

try:
    from joblib import Parallel, delayed
except:
    print 'Joblib is not installed. Using standard multiprocessing.'
    joblib_available = False
else:
    joblib_available = True

parser = ArgumentParser()
parser.add_argument('-c', '--chunks', nargs='?', type=int, help='Number of chunks to load')
parser.add_argument('-f', '--filenames', nargs='+', type=str, help='Filename for the log')
parser.add_argument('-o', '--output', nargs='?', type=str, default='output.
