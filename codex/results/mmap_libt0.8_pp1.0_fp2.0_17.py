import mmap
import sys

from os.path import isfile
from StringIO import StringIO
from pandas import DataFrame, concat, read_table
from Bio import SeqIO


def raxml_tree(aln, outdir='.', sf=None):
    """
    Run RAxML to build a tree on a Phylip-format alignment file (aln)
    using a data-partition file (sf).
    """
    if not isfile(aln):
        raise IOError('{0} does not exist'.format(aln))
    if sf is not None and not isfile(sf):
        raise IOError('{0} does not exist'.format(sf))

    # Generate a temporary control file for RAxML
    treefile = join(outdir, splitext(basename(aln))[0]) + '.raxml'
    tmpfile = join(outdir, 'RAxML_info.{0}'.format(basename(aln)))
    raxmlc = ('raxmlHPC-AVX -T 16 -s {al
