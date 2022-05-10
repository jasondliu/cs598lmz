import mmap
import os
import re
import subprocess
import sys
import tempfile
import time

from . import config
from . import constants
from . import util

# FIXME: These should be moved to a common module.
def _get_path_to_binary(binary_name):
  """Returns the path to a binary.

  Args:
    binary_name: The name of the binary.

  Returns:
    The path to the binary.
  """
  return os.path.join(config.GetOutDirectory(), binary_name)


def _get_path_to_tool_binary(tool_name):
  """Returns the path to a tool binary.

  Args:
    tool_name: The name of the tool.

  Returns:
    The path to the tool binary.
  """
  return _get_path_to_binary('%s_tool' % tool_name)


def _get_path_to_test_binary(test_name):
  """Returns the path to a test binary.

  Args:
    test_name: The name of the
