from lzma import LZMADecompressor
LZMADecompressor().decompress(data_as_bytes)

data = msgpack.unpackb(data_as_bytes)
data

# Cleanup
del data, data_as_bytes
gc.collect();

# Then I tried gzip.

import gzip
from gzip import GzipFile
from io import BytesIO
gzip.open(BytesIO(data_as_bytes))

# I haven't found a way to make the operation truly transparent, but this works:

import gzip
from gzip import GzipFile
from io import BytesIO
from lzma import LZMADecompressor
from lzma import LZMAFile
from glob import glob
from pathlib import Path
from io import BytesIO
from lzma import LZMADecompressor
from lzma import FORMAT_XZ
from lzma import LZMAError
from contextlib import suppress
from subprocess import check_output
from operator import itemgetter
from itertools import groupby
from shutil import copyfile
from collections import OrderedDict
from ast import
