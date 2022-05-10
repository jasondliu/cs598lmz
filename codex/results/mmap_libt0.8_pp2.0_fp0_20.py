import mmap
import os.path
import platform
import re
import shlex
import subprocess
import sys
import threading
import time

import six

from . import command_utils


# The size of the remote files sent to the kernel
CHUNK_SIZE = 1048576

# The default amount of time to wait for a kernel to finish.
#
# 5 minutes is the default waiting time for Debian Linaro Ubuntu images, but
# this value has been increased to 10 minutes to account for cross-compilation
# overheads on Arch Linux.
DEFAULT_WAIT_TIME = 10 * 60

# A timeout value of 0 means no timeout
NO_TIMEOUT = 0

# The maximum amount of time to wait for a kernel to finish, running a "test"
# suite.
TEST_WAIT_TIME = 15 * 60

# The default amount of time to wait for a kernel to finish running a set
# of tests without asserting that a mandatory test passes.
TEST_WAIT_TIME_SHORT = 5 * 10

# The default amount of time to wait for a kernel to finish running a set

