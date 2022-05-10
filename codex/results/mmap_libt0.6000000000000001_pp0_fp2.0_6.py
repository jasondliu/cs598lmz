import mmap
import os
import sys
import time
import threading

from .base import Base
from .context import Context
from .event_handler import EventHandler
from .file_monitor import FileMonitor
from .file_watcher import FileWatcher
from .logger import Logger
from .matcher import Matcher
from .notifier import Notifier
from .reloader import Reloader
from .runner import Runner
from .signal_handler import SignalHandler
from .spawner import Spawner
from .state import State
from .statistics import Statistics

class Daemon(Base):
    """
    A daemon that watches a list of file paths and runs a command when a change
    is detected.
    """

    def __init__(self, args):
        """
        :type args: list
        """

        super(Daemon, self).__init__()

        self.args = args

        self.context = Context()
        self.event_handler = EventHandler()
        self.file_monitor = FileMonitor()
        self.file_watcher = FileWatcher()
        self.logger =
