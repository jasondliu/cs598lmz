import mmap
import numpy as np
import os
import pandas as pd
import re
import sys
import time

from collections import Counter
from multiprocessing import Pool
from multiprocessing.dummy import Pool as ThreadPool

from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio.SeqIO import FastaIO
from Bio.Alphabet import generic_dna

from pyfaidx import Fasta

from pysam import FastaFile

from scipy.sparse import csr_matrix

from sklearn.decomposition import PCA

from statsmodels.stats.multitest import multipletests

# load in the configuration file
with open('../config.yaml') as f:
    config = yaml.load(f)
