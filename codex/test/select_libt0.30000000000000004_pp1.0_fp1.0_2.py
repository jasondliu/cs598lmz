import select
import subprocess
import sys
import time

import psutil

from . import utils
from . import __version__


def _get_logger():
    return logging.getLogger(__name__)


def _get_process_info(pid):
    try:
        process = psutil.Process(pid)
    except psutil.NoSuchProcess:
        return None
    return {
        'pid': pid,
        'name': process.name(),
        'cmdline': process.cmdline(),
        'cpu_percent': process.cpu_percent(),
        'memory_percent': process.memory_percent(),
        'memory_info': process.memory_info(),
    }


class ProcessMonitor(object):
    def __init__(self, pid, interval=1, log_file=None, log_level=logging.INFO):
        self.pid = pid
        self.interval = interval
        self.log_file = log_file
        self.log_level = log_level

        self.logger = _get_logger()
       
