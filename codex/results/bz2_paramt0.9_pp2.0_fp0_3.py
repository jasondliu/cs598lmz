from bz2 import BZ2Decompressor
BZ2Decompressor.decompress_check_size = lambda self, data, max_length: self.decompress(data, max_length)

import io, gc, os
import pytest
import tempfile

from dask.bytes import open_files
import dask.bytes.core
import numpy as np
from dask.utils import tmpfile, tmpdir
import pandas as pd
from dask.bytes.utils import infer_storage_options
from dask.bytes.compression import files as compression
import dask.dataframe as dd
from dask.dataframe.utils import assert_eq, PANDAS_GT_050, PANDAS_GT_07

from dask.bytes.core import read_bytes, open_files, open_text_files, read_text
from dask.bytes.compression import seekable_files, seekable_file
from dask.bytes.compression.compressors import (BZ2File, GzipFile, LZMAFile,
    compute_chunksize)
from dask.bytes.core import get_fs_token_paths
