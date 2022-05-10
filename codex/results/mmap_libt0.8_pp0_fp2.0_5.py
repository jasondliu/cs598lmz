import mmap
from collections import defaultdict
import StringIO
import copy

from segment import Segment
from utils import parse_position, get_ref
from error import InvalidPositionError
from error import InvalidSegmentError
from error import InvalidGenotypeError


class VcfFile(object):
    """
    Class representing a VCF file.
    """
    def __init__(self, fp):
        self.fp = fp
        self.mm = mmap.mmap(fp.fileno(), 0, prot=mmap.PROT_READ)
        line_idx = self.mm.find('\n') + 1
        line = self.mm[:line_idx].rstrip()
        if not line.startswith('#CHROM'):
            raise InvalidVcfFileError(
                'Not a valid VCF file. Missing header information.'
            )
        header = line.split('\t')
        try:
            idx_chrom = header.index('#CHROM')
            idx_pos = header.index('POS')
            idx_id = header
