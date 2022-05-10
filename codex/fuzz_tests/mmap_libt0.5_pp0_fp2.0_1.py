import mmap
import os
import re
import sys
import tempfile
import threading
import time
import traceback

from . import common
from . import config
from . import constants
from . import git
from . import gsutil
from . import log
from . import metrics
from . import patch
from . import stats
from . import test_failures
from . import test_utils
from . import utils
from . import xvfb
from .test_utils import BINARY_DEPS

# Aliases for readability.
SUCCESS = constants.SUCCESS
WARNINGS = constants.WARNINGS
FAILURE = constants.FAILURE
SKIPPED = constants.SKIPPED

# Global variables to be used by the main thread.
THREADS = []
EXCEPTIONS = []

# Global variables to be used by the main thread and the child threads.
# Note: This is a lock for the global variables in the main thread.
#       It is used to protect the accesses to the global variables in the
#       main thread from the child threads.
LOCK = threading.Lock()

