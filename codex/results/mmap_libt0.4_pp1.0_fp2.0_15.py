import mmap
import os
import re
import sys

from collections import defaultdict
from glob import glob
from os.path import abspath, basename, dirname, expanduser, getsize, isdir, isfile, join, splitext
from subprocess import Popen, PIPE

from . import __version__
from . import utils
from . import constants

# ------------------------------------------------------------------------------
# Classes
# ------------------------------------------------------------------------------

class Reads(object):
    """
    Class for reads.
    """

    def __init__(self,
                 fastq_fp,
                 fastq_format=None,
                 quality_offset=None,
                 min_quality=None,
                 max_ambiguous=None,
                 max_homopolymer=None,
                 max_primer_mismatch=None,
                 max_barcode_mismatch=None,
                 max_bad_run_length=None,
                 max_low_quality_bases=None,
                 min_length=None,
                 max_length=None,
                 truncate_ambiguous=False,
                
