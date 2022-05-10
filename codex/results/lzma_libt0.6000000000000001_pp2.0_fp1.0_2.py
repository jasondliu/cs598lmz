import lzma
lzma.__doc__ = """
LZMA (Lempel-Ziv-Markov chain-Algorithm) compression.

This module provides a comprehensive interface for the
compression and decompression of data using LZMA compression
based on XZ Utils C library (http://tukaani.org/xz/).

See https://docs.python.org/3/library/lzma.html for more information.
"""
from _lzma import *

from _lzma import __doc__
from _lzma import __all__
from _lzma import __version__
