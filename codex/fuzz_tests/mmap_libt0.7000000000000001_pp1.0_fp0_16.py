import mmap
import optparse
import os
import pty
import re
import select
import signal
import socket
import stat
import string
import subprocess
import sys
import termios
import threading
import time
import traceback

import katcp
import katcp.kattypes

from optparse import OptionParser

# Some constants used in the protocol

REQUEST = 0
REPLY = 1
INFORM = 2

# TODO: auto-generate from spec
VERSION_MAJOR = 5
VERSION_MINOR = 3

EOS = '\n\n'  # End of string
EOL = '\n'  # End of line

DEFAULT_HELP_WIDTH = 80

# TODO:  make the timeout configurable
REQUEST_TIMEOUT = 5.0

# TODO:  make the timeout configurable
INFORM_TIMEOUT = 5.0

# This is the encoding used for byte-strings.
BYTE_ENCODING = "latin-1"


class Message(object):
    """A KATCP message
