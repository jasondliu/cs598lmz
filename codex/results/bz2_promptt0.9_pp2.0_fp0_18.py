import bz2
# Test BZ2Decompressor
from gzip import GzipFile
from gzip import compress as gz_compress
from gzip import decompress as gz_decompress
from bz2 import BZ2File
from bz2 import compress as bz2_compress
from bz2 import decompress as bz2_decompress
from tempfile import TemporaryFile
# Test ZlibCompressoe and ZlibDecompress
from zlib import compress as z_compress
from zlib import decompress as z_decompress
from hashlib import md5
from time import time

from numpy import arange
try:
    from theano.gof.argsort import argsort
except ImportError:
    from theano.tensor.argsort import argsort
# XXX: Reorder the mp imports for each backend
from theano.compile import ReinterpretCast
from theano.tensor import (TensorType, tensor, dscalar, dvector,
                           ivector, filter, dtensor3, tensor3,
                           vector, Tensor, TensorFromScalar,

