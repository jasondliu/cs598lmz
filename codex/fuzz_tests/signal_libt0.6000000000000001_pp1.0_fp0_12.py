import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

# https://www.gnu.org/software/libc/manual/html_node/Nonreentrant-Functions.html#Nonreentrant-Functions
import sys
if sys.platform == "win32":
    import msvcrt
    msvcrt.setmode(sys.stdin.fileno(), os.O_BINARY)
    msvcrt.setmode(sys.stdout.fileno(), os.O_BINARY)
    msvcrt.setmode(sys.stderr.fileno(), os.O_BINARY)

import os
import os.path
import getopt
import socket
import struct
import select
import errno
import hashlib
import zlib
import array
import fcntl
import time
import math
import threading
import traceback
import Queue
import subprocess
import atexit
import logging

try:
    import ssl
except ImportError:
    ssl = None

import xpra
