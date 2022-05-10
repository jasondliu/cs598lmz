import mmap
import argparse
import sys

# TODO: This is to prevent a bug in Mac OS X.  Remove when Apple fixes the OS.
# See: http://bugs.python.org/issue10394
# FIXME: This is a hack!
try:
    import multiprocessing
except ImportError:
    pass

import pybedtools
from pybedtools import BedTool
from pybedtools.featurefuncs import gff2bed, gtf2bed
from pybedtools.contrib.bigwig import bigwig2bed
from pybedtools.contrib.gff2bed import gff2bed_cl
from pybedtools.contrib.gtf2bed import gtf2bed_cl
from pybedtools.contrib.two_bit import twoBitToFa
from pybedtools.contrib.bigbed import bigbed2bed
from pybedtools.contrib.bigwig import bigwig2bed
from pybedtools.contrib.seq_crumbs import fasta2dict, fastq2dict
from pybedtools.contrib.twobit import TwoBitFile
from py
