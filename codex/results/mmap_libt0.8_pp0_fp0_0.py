import mmap
import os
import re
import shutil
import socket
import stat
import subprocess
import sys
import tempfile
import threading
import time
import traceback

from datetime import datetime
from optparse import OptionParser
from subprocess import Popen
from subprocess import PIPE

from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler


#TODO: enable git integration
#TODO: enable on-the-fly mode (read: disable interrupts)
#TODO: implement command timeout


# Exit codes
EXIT_SUCCESS = 0
EXIT_FAILURE = 1
EXIT_INVALID_ARGS = 2

# Termination signals
TERMINATE_SIGNALS = [
    signal.SIGTERM,
    signal.SIGQUIT,
    signal.SIGINT
]

# Default config file
FILE_CONFIG_DEFAULT = "dokuflame.conf"
# Config file regex
FILE_CONFIG_REGEX = r"dokuflame\.(conf|json)"

# Default
