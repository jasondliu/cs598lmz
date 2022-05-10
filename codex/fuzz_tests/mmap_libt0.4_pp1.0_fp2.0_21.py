import mmap
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time
import traceback

from . import config
from . import constants
from . import errors
from . import file_util
from . import git
from . import log
from . import util

from . import build_util
from . import log_util
from . import process_util
from . import subprocess_util


def _get_android_sdk_dir():
  """Returns the path to the Android SDK directory."""
  if config.ANDROID_SDK_ROOT:
    return config.ANDROID_SDK_ROOT
  return os.path.join(config.CHROME_DIR, 'third_party', 'android_tools',
                      'sdk')


def _get_android_ndk_dir():
  """Returns the path to the Android NDK directory."""
  if config.ANDROID_NDK_ROOT:
    return config.ANDROID_NDK_ROOT
  return os.path.join(config.CHROME_DIR,
