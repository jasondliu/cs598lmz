from bz2 import BZ2Decompressor
BZ2Decompressor
from multiprocessing import Pool
from multiprocessing.dummy import Pool as ThreadPool
from collections import Counter
import gzip
import shutil
import sys
from datetime import datetime
from multiprocessing import Process, Manager


#from itertools import izip_longest
def grouper(iterable, n, fillvalue=None):
    "Collect data into fixed-length chunks or blocks"
    # grouper('ABCDEFG', 3, 'x') --> ABC DEF Gxx"
    args = [iter(iterable)] * n
    return zip_longest(*args, fillvalue=fillvalue)


def Define_qval_cutoff(qvals):
    thresholds=list(range(5,20,5))
    counts=[int(sum(1 for x in qvals if x>thresh)) for thresh in thresholds]
    cutoff=thresholds[counts.index(max(counts))]
    return cutoff

def Define_phred_cutoff(phreds):
    phreds=np.array(phreds)
   
