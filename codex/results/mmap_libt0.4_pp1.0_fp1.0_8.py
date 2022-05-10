import mmap
import os
import re
import sys
import tarfile
import tempfile
import zipfile

from six.moves import urllib

from tensorflow.python.platform import gfile
from tensorflow.python.util.all_util import make_all

# pylint: disable=g-import-not-at-top
try:
  import bz2file
except ImportError:
  bz2file = None
# pylint: enable=g-import-not-at-top


def _read_url(url):
  """Read the contents of a URL.

  Args:
    url: Source URL.

  Returns:
    Contents of the URL.
  """
  with contextlib.closing(urllib.request.urlopen(url)) as url_file:
    return url_file.read()


def _read_file(filename):
  """Read the contents of a file.

  Args:
    filename: Source file.

  Returns:
    Contents of the file.
  """
  with open(filename, 'rb
