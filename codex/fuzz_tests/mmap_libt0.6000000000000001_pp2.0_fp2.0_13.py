import mmap
import os
import re
import subprocess
import shutil
import sys
import tempfile
import threading
import time

from optparse import OptionParser

import utils

# This is the maximum amount of time we will wait for a process to
# exit after we have asked it to exit.
MAX_WAIT_TIME_SECONDS = 60

# This is the maximum amount of time we will wait for a process to
# exit after we have sent it a kill (SIGKILL).
MAX_FORCE_WAIT_TIME_SECONDS = 10

# This is the maximum amount of time we will wait for a process to
# exit after we have sent it a SIGTERM.
MAX_TERM_WAIT_TIME_SECONDS = 5

# This is the maximum amount of time we will wait for a process to
# exit after we have sent it a SIGINT.
MAX_INT_WAIT_TIME_SECONDS = 5

# This is the amount of time we will wait for a process to exit before
# we check its status again.
WAIT_TIME_INCRE
