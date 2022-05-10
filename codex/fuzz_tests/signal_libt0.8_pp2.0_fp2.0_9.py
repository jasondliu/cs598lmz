import signal
signal.signal(signal.SIGPIPE, signal.SIG_DFL)
import gc
import argparse
import pysam
import numpy as np
import pyfaidx
from tqdm import tqdm
import pandas as pd
import multiprocessing as mp
from numba import jit
from subprocess import check_call, run, PIPE
from Bio import SeqIO
from tempfile import NamedTemporaryFile
import subprocess
# local imports
#from utils.misc import *
#from utils.io import *
#from utils.online_kmer_counter import kmer_counter

# from:
# https://github.com/dpryan79/phylogenetic_assembly/blob/master/utils/kmer_counter.py

def revcomp(seq):
    return "".join([{"A":"T","C":"G","G":"C","T":"A"}[s] for s in reversed(seq.rstrip())])

@jit(nopython=False)
def kmer_counter(seq, ksize
