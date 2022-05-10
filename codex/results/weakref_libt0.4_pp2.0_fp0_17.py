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

    def __init__(self, source, metadata=None, common_metadata=None,
                 open_with=None, buffer_size=None, memory_map=False,
                 use_threads=True, use_pandas_metadata=False,
                 split_row_groups=False, validate_schema=True,
                 use_deprecated_int96_timestamps=False,
                 ignore_metadata_columns=False,
                 ignore_empty_partitions=False,
