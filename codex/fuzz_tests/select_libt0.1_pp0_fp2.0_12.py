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
from . import xlog
from . import xlogviewer
from . import xlogserver

class XLogClient(object):
    def __init__(self, host, port, log_dir, log_level, log_file, log_max_size, log_backup_count, log_stdout, log_stderr, log_rotate_when, log_rotate_interval, log_rotate_fmt, log_rotate_utc, log_rotate_mode, log_rotate_at, log_rotate_at_time, log_rotate_at_interval, log_rotate_at_backup_count, log_rotate_when_size, log_rotate_when_size_max, log_rotate_when_size_interval, log_rotate_when_size_backup_count, log_rotate_when_size_fmt, log_rotate
