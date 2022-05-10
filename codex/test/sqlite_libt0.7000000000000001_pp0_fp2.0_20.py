import ctypes
import ctypes.util
import threading
import sqlite3
import os
import sys
import json
import logging
import collections
from collections import OrderedDict
from subprocess import Popen, PIPE


# Constants
# ---------

_HELP_MESSAGE = """
Usage: btrfs-subvolume-snapshot [OPTION]... DEST SRC
Create a snapshot of SRC at DEST.

-k, --keep-snapshots              do not automatically delete old snapshots
-p, --prefix PREFIX               prefix for all snapshots
-d, --date-suffix                 add a date suffix to the snapshot name
-f, --fsync                       fsync all parent directories and the snapshot
-a, --atomic-read-only            create a readonly snapshot
-n, --no-atomic-read-only         create a read-write snapshot
-s, --silent                      do not output any status messages
-t, --timeout TIMEOUT             timeout for the snapshot
-x, --exclude PATTERN             exclude files matching PATTERN
--help                            display this help and exit
--version                         output version information and exit
"""

_VERSION_M
