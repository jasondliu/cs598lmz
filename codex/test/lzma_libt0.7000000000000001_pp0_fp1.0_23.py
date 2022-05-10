import lzma
lzma_compress = lzma.compress
lzma_decompress = lzma.decompress

# TODO: add support for lz4 and brotli

from typing import Union, Tuple, Optional
from hashlib import blake2b
from binascii import hexlify
from base64 import b64encode
from marshal import loads, dumps
from itertools import product
from pprint import pformat
