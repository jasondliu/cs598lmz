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

from google.protobuf.pyext import _message
from google.protobuf.internal import enum_type_wrapper
from google.protobuf.internal import containers
from google.protobuf.internal import decoder
from google.protobuf.internal import encoder
from google.protobuf.internal import wire_format
from google.protobuf.internal import type_checkers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
