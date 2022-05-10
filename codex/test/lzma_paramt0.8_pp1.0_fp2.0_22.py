from lzma import LZMADecompressor
LZMADecompressor()
from gzip import decompress
from bz2 import decompress
from tarfile import TarFile
from tarfile import TarError
import argparse

from pathlib import Path
from functools import partial
from itertools import chain
from contextlib import contextmanager
from multiprocessing import Pool
from multiprocessing.pool import ThreadPool
from collections import OrderedDict, defaultdict, namedtuple

from typing import *
from types import SimpleNamespace

