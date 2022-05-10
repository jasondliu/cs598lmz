import mmap
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time

from . import _pybind_utils
from . import _utils
from . import _version
from . import _xla_bridge

# pylint: disable=g-import-not-at-top
try:
  from typing import Any, Dict, List, Optional, Text, Tuple, Union
except ImportError:
  pass

# pylint: disable=g-import-not-at-top
try:
  from tensorflow.python.platform import tf_logging as logging
except ImportError:
  from tensorflow.python.platform import logging

# pylint: disable=g-import-not-at-top
try:
  # pylint: disable=g-import-not-at-top
  import tensorflow.compiler.xla.python.xla_extension as xla_extension
except ImportError:
  # pylint: disable=g-import-not-at-top
  import xla_extension
