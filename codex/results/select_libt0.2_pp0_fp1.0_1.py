import select
import socket
import sys
import threading
import time
import traceback

from . import __version__
from . import config
from . import constants
from . import errors
from . import log
from . import utils
from . import xlogging

_logger = xlogging.getLogger(__name__)

_g_lock = threading.Lock()
_g_threads = []
_g_threads_event = threading.Event()


class _Thread(threading.Thread):
    def __init__(self, name, target, args=None, kwargs=None):
        super(_Thread, self).__init__(name=name, target=target, args=args, kwargs=kwargs)
        self.daemon = True

    def run(self):
        with _g_lock:
            _g_threads.append(self)
        try:
            super(_Thread, self).run()
        except Exception as e:
            _logger.error(r'_Thread.run failed : {}'.format(e), exc_
