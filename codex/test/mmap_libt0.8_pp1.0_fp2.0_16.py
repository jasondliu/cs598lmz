import mmap
from pathlib import Path
import ctypes
import gzip
import os.path
from collections import namedtuple
from typing import Union

from Bio.Seq import Seq, MutableSeq
from Bio.SeqRecord import SeqRecord

from . import util


def mmap_open(path: Union[str, Path], mode: str) -> mmap.mmap:
    """
    Open a file, get a memory map, and close the file.
    """
