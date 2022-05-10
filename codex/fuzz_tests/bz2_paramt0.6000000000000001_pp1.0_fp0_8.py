from bz2 import BZ2Decompressor
BZ2Decompressor()

try:
    import lzma
except ImportError:
    from backports import lzma

try:
    import zstandard as zstd
except ImportError:
    zstd = None

import contextlib
from collections import defaultdict
from collections.abc import Iterable
from functools import wraps
from io import BytesIO
from itertools import chain, cycle, repeat
from pathlib import Path
import re
import struct
from typing import (
    Any,
    BinaryIO,
    DefaultDict,
    Dict,
    Iterator,
    List,
    Optional,
    Tuple,
    Type,
    Union,
)
from zipfile import ZipFile
from zlib import decompressobj

from pkg_resources import Requirement

from .exceptions import (
    BadZipFile,
    EOFHeaderError,
    EOFError,
    FileModeError,
    InvalidHeader,
    InvalidMagicError,
    InvalidPathError,
    NoHeaderError,
    NotSeekable,
    ReadError,
    UnsupportedCompression
