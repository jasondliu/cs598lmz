import mmap
import os
import sys
import tarfile
import tempfile
import zipfile

from six.moves import urllib

from tensorflow.python.framework import dtypes
from tensorflow.python.framework import random_seed
from tensorflow.python.platform import gfile
from tensorflow.python.util.tf_export import tf_export

# pylint: disable=g-import-not-at-top
try:
  import scipy.io as sio
except ImportError:
  pass
# pylint: enable=g-import-not-at-top


def _read32(bytestream):
  """Read 4 bytes from bytestream as an unsigned 32-bit integer."""
  dt = numpy.dtype(numpy.uint32).newbyteorder('>')
  return numpy.frombuffer(bytestream.read(4), dtype=dt)[0]


@tf_export('image.extract_gzip')
def extract_gzip(filepath, num_images=1):
  """Extract the
