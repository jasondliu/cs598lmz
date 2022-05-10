import weakref
import yaml

from parabam.bam import Bam
from parabam.pileup import Pileup
from parabam.summary import Summary


def get_bam_path(path):
    """Returns the path to the BAM file given a path to a parabam file."""
    fragments = path.split('.')
    fragments[-1] = 'bam'
    return '.'.join(fragments)


class Parabam:

    def __init__(self, path, logger=None):
        self._path = path
        self._bam_path = get_bam_path(self._path)
        self._logger = logger
        self._bam = None
        self._pileup = None
        self._summary = None
        self._metadata = {}
        self._reference_name = None
        self._reference_length = None
        self._reference_md5 = None
        self._reference_file = None
        self._reference_file_md5 = None
        self._reference_assembly = None
        self._
