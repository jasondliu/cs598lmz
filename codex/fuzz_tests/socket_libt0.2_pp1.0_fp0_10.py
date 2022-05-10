import socket
import sys
import time
import threading
import traceback

from . import common
from . import config
from . import log
from . import util
from . import version
from . import worker
from . import xlog

class Master(object):
    def __init__(self):
        self.config = config.Config()
        self.config.load(self.config.master_config)
        self.config.check()

        self.log_dir = self.config.get("log_dir")
        self.pid_file = self.config.get("pid_file")
        self.log_file = os.path.join(self.log_dir, "master.log")
        self.log_level = self.config.get("log_level")
        self.log_max_bytes = self.config.get("log_max_bytes")
        self.log_backup_count = self.config.get("log_backup_count")
        self.log_rotate_when = self.config.get("log_rotate_when")
        self.log
