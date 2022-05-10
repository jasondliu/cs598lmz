import gc, weakref
import threading

from . import log
from . import util
from . import config as _config

#
# Manage the lifecycle of a single process, which can be a daemon
# or a client
#

class Process:
    # Lifecycle state
    NEW, STARTING, RUNNING, STOPPING, STOPPED, ERROR = range(0,6)

    def __init__(self, pid, name, uri, config, plugins, proc_factory):
        self.pid = pid
        self.name = name
        self.uri = uri
        self.config = config
        self.plugins = plugins

        self.proc_factory = proc_factory
        self.proc = None
        self.state = Process.NEW

        # List of non-daemon processes that depend upon us
        self.dependents = []

        # List of non-daemon processes that we depend upon
        self.dependencies = []

        self.lock = threading.RLock()

    @property
    def daemon(self):
        return self.proc_factory.da
