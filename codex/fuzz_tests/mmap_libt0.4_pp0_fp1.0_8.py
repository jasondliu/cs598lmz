import mmap
import os
import pprint
import re
import shutil
import struct
import subprocess
import sys
import tempfile
import time
import zipfile

import common
import test_utils
from test_utils import (
  AdbError,
  DeviceError,
  DeviceUnresponsiveError,
  TimeoutError,
  WaitForResponseTimedOutError,
  WaitForStateTimedOutError,
  )

OPTIONS = common.OPTIONS
OPTIONS.verbose = False
OPTIONS.test_device = None
OPTIONS.device_specific = None
OPTIONS.device_specific_dir = None
OPTIONS.log_to_file = False
OPTIONS.log_to_stdout = False
OPTIONS.log_dir = None
OPTIONS.log_file = None
OPTIONS.log_file_mode = 'w'
OPTIONS.log_file_max_size = 1024 * 1024 * 1024
OPTIONS.log_file_count = 5
OPTIONS.log_file_level = logging.INFO
OP
