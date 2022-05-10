import lzma
lzma.LZMAFile

import os
import sys
import time
import json
import pickle
import logging
import argparse
import subprocess
import multiprocessing
import traceback

from collections import defaultdict
from multiprocessing import Pool
from multiprocessing import Manager

from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio.Alphabet import generic_dna

from . import utils
from . import config
from . import __version__

logger = logging.getLogger(__name__)

def parse_args(args):
    parser = argparse.ArgumentParser(
        description='Finds the best match for each read in a set of reads to a set of reference sequences.',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('--version', action='version',
                        version='%(prog)s {version}'.format(version=__version__))

    parser.add_argument('--reads', type=str,
