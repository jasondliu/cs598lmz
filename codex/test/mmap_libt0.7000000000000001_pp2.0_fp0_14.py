import mmap
import os
import sys
import subprocess
import signal

from pprint import pprint
from . import config
from . import log

# global reference to buffered input
input_buffer = None

# global reference to buffered output
output_buffer = None

# global reference to child process
child = None
