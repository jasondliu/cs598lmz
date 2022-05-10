import mmap
import os
import re
import sys
import time
import traceback

from . import config
from . import log
from . import util
from . import version

# The following are used to determine the default value of the
# --max-jobs option.
_DEFAULT_MAX_JOBS = None
_DEFAULT_MAX_JOBS_IS_SET = False

# The following are used to determine the default value of the
# --max-load option.
_DEFAULT_MAX_LOAD = None
_DEFAULT_MAX_LOAD_IS_SET = False

# The following are used to determine the default value of the
# --max-load-average option.
_DEFAULT_MAX_LOAD_AVERAGE = None
_DEFAULT_MAX_LOAD_AVERAGE_IS_SET = False

# The following are used to determine the default value of the
# --max-load-average-per-job option.
_DEFAULT_MAX_LOAD_AVERAGE_PER_JOB = None
_DEFAULT_MAX_LOAD_AVERAGE_PER_JOB_IS_SET
