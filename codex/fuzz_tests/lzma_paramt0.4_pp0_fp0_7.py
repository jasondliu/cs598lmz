from lzma import LZMADecompressor
LZMADecompressor

import numpy as np
from numpy.testing import assert_equal
from numpy.testing import assert_array_almost_equal
from numpy.testing import assert_array_equal
from numpy.testing import assert_raises
from numpy.testing import assert_warns

from skimage.io._plugins.freeimage_plugin import (
    freeimage_to_array,
    array_to_freeimage,
    _freeimage_available,
    _freeimage_version,
)


def setup():
    if not _freeimage_available:
        raise SkipTest('FreeImage library not available')


def teardown():
    pass


def _load_test_image(fname):
    f = open(fname, 'rb')
    try:
        return np.load(f)
    finally:
        f.close()


def _load_test_image_lzma(fname):
    f = open(fname, 'rb')
    try:
        return np.load(LZMADecompressor().stream(f))
   
