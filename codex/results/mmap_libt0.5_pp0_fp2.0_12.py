import mmap
import shutil
import tempfile
import unittest

from six.moves import urllib

from tensorflow.core.example import example_pb2
from tensorflow.core.example import feature_pb2
from tensorflow.core.example import feature_util
from tensorflow.core.example import example_parser
from tensorflow.python.framework import dtypes
from tensorflow.python.framework import errors
from tensorflow.python.framework import ops
from tensorflow.python.lib.io import python_io
from tensorflow.python.ops import io_ops
from tensorflow.python.ops import parsing_ops
from tensorflow.python.ops import variables
from tensorflow.python.platform import gfile
from tensorflow.python.platform import test


class ExampleParserTest(test.TestCase):

  def setUp(self):
    self._num_files = 2
    self._num_records = 7
    self._test_filenames = self._CreateFiles()

  def tearDown(self):
    for filename in
