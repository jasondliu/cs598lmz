import mmap

from collections import OrderedDict
from itertools import izip

import struct
import numpy as np

from . import utils
from .utils import peek
from .utils import little_endian_to_int as le2i
from .utils import little_endian_to_float as le2f

from . import context
from .context import get_context

from . import logger
from .logger import get_logger

from . import constants

__all__ = ['BVHReader', 'BVHWriter']

LOG = get_logger(__name__)

class BVHReader(object):

    def __init__(self, filepath):
        self.filepath = filepath

        self.file = open(self.filepath, 'r')
        self.mmap = mmap.mmap(self.file.fileno(), 0, prot=mmap.PROT_READ)

        self.header = {}
        self.joints = []

        self.context = get_context()

        self.parse_header()
