import weakref
import sys
import os.path

from cortex.utils import set_thread_name
from cortex.utils.synchronization import Mutex, ConditionVariable
from cortex.plugins import Plugin
from cortex.utils.logger import Logger
from cortex.proto import Definition_pb2
from cortex.utils.object_registry import ObjectRegistry

_log = Logger.getLogger('Cortex.Server')

class Module(object):
    """
    This class is the base class for all modules implementing a Cortex service.
    """

    def __init__(self, server):
        self.server = server
        self.sockets = []
        self.yields = {}
        self.module_refs = {}
        self.mutex = Mutex()

    @property
    def _yield_cv(self):
        try:
            return self.yields[self._current_socket]
        except KeyError:
            self.yields[self._current_socket] = cv = ConditionVariable(self.mutex)
            return cv
