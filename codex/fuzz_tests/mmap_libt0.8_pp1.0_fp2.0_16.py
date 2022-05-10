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
    f = open(path, mode)
    m = mmap.mmap(f.fileno(), 0)

    # The mmap will keep the file descriptor open until the mmap is closed.
    f.close()

    return m


def mmap_mmap(path: Union[str, Path], mode: str,
              offset: int=0, length: int=0,
              access: int=mmap.ACCESS_COPY) -> mmap.mmap:
    """
    Get a memory map from an existing file.
    """
    f = open(path, mode)
   
