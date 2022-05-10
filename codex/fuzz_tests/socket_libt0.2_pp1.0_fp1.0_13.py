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
from . import xlogviewer_pb2

_logger = log.get_logger(__name__)


class XlogViewerServer(xlogserver.XlogServer):
    def __init__(self, xlog_dir, port, max_log_size, max_log_count,
                 max_log_age, max_log_age_units, max_log_age_units_str,
                 max_log_age_str, max_log_count_str, max_log_size_str,
                 max_log_size_units, max_log_size_units_str,
                 max_log_size_units_str_plural,
                 max_log_size_units_str_singular,
                 max_log_size_units_str_plural_abbrev,
                 max_log
