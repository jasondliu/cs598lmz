from bz2 import BZ2Decompressor
BZ2Decompressor()
# note: should work with py 2.6+

from mmap import mmap
from collections import deque
from operator import itemgetter
from collections import namedtuple

from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord

from fcy.numeric import digit_to_base, base_to_digit


def get_fastx_data(handle, index=None):
    """
    Reads FASTX data from a handle.

    Takes in data from a FASTA or FASTQ file and returns a generator of tuples
    (data, params).  Data may be a list of strings for each line in the file,
    a list of strings containing the ids and sequences for each entry in the
    file, or a list of lists containing the full data for each sequence record
    in the file, depending on whether indexing is on or off.

    If indexed = True, returns a list of tuples:
    (id_line, sequence)
    as well as the index.

    If indexed = False, returns a list of
