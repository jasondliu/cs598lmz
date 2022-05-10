import signal
signal.signal(signal.SIGPIPE, signal.SIG_DFL)

sys.path.append('..')

import Bio
from Bio import SeqIO
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio.Alphabet import generic_dna
from Bio.Alphabet import generic_protein

#from bx.bbi.bigwig_file import BigWigFile
import bx.bbi.bigwig_file
import argparse

import gzip

try:
    from collections import OrderedDict
except ImportError:
    from ordereddict import OrderedDict

import util
import qc

import scipy.stats
import seaborn as sns

import MySQLdb
import bx.bbi.bigwig_file
import numpy as np
import numpy.random
import subprocess

import math 

import random

import os


