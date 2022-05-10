import weakref
from typing import List

from . import _ffi
from . import _lib
from . import _util
from . import _errors
from . import _metadata
from . import _compression
from . import _types
from . import _tables
from . import _block_cache
from . import _column
from . import _writer
from . import _reader
from . import _util
from . import _schema
from . import _encoding


class File(object):
    """
    A Parquet file.

    This class is the main entry point for reading and writing Parquet files.
    """

