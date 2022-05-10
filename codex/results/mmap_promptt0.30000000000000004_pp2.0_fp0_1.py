import mmap
# Test mmap.mmap(0, 1, "shared", mmap.MAP_SHARED)

import os
import re
import subprocess
import sys
import time

import numpy as np

from . import _pywrap_tensorflow_internal as _pywrap_tensorflow
from . import errors
from . import pywrap_tensorflow
from . import version
from .framework import dtypes
from .framework import errors_impl
from .framework import graph_pb2
from .framework import importer
from .framework import ops
from .framework import tensor_shape
from .framework import tensor_util
from .framework import types
from .framework import versions
from .util import compat
from .util import deprecation
from .util.deprecation import deprecated

# pylint: disable=g-import-not-at-top
try:
  from tensorflow.python.util import module_wrapper as deprecation_wrapper
except ImportError:
  from tensorflow.python.util import deprecation_wrapper
# pylint: enable=g-import-not-at-top


