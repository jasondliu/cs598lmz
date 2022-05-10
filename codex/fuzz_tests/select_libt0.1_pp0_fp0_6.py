import select
import socket
import sys
import threading
import time
import traceback

from . import config
from . import log
from . import util
from . import version

# This is the maximum number of bytes we'll read from a socket at a time.
# This is also the maximum number of bytes we'll write to a socket at a time.
# This is also the maximum number of bytes we'll read from a file at a time.
# This is also the maximum number of bytes we'll write to a file at a time.
# This is also the maximum number of bytes we'll read from a pipe at a time.
# This is also the maximum number of bytes we'll write to a pipe at a time.
# This is also the maximum number of bytes we'll read from a tty at a time.
# This is also the maximum number of bytes we'll write to a tty at a time.
# This is also the maximum number of bytes we'll read from a serial port at a time.
# This is also the maximum number of bytes we'll write to a serial port at a time.
# This is also the maximum number of bytes we'll read
