import mmap
import struct
import argparse
import hashlib
from io import BytesIO

from . import readelf
from . import pe
from .errors import *

class BinaryFile(object):
    def __init__(self):
        self.path = None
        self.wordsize = None
        self.endianity = None
        self.arch = None
        self.os = None
        self.executable = None
        self.initialized_data = None
        self.uninitialized_data = None
        self.readonly_data = None
        self._fd = None
        self._mmap = None

    def _create_mmap(self, fd, length, flags, prot, offset=0, advice=mmap.MADV_NORMAL):
        retval = mmap.mmap(fd, length, flags, prot, offset, advice)
