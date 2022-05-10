import mmap
from datetime import datetime
from operator import itemgetter
from collections import defaultdict
from multiprocessing import Pool

from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio.Alphabet import IUPAC
from Bio.SeqUtils import GC
from Bio.SeqUtils import MeltingTemp as mt

from roblib import bcolors
from roblib import stream_fasta
from roblib import stream_fastq
from roblib import revcomp
from roblib import read_fastq
from roblib import read_fasta
from roblib import colours as col


