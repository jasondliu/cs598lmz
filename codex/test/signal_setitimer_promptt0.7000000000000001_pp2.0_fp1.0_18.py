import signal
# Test signal.setitimer
import time
from test import support
from test.support import import_module
thread = import_module('thread')
threading = import_module('threading')


class Timeout(Exception):
    """Exception raised when a timeout occurs."""


class SignalHandler:
    """Facility for testing signal handling in threads.

    This class installs a SIGALRM handler and provides a method
    to raise a Timeout exception in a separate thread.
    """

    def __init__(self):
        """Initialize the instance."""
        self._raised = False
        self._event = threading.Event()
        self._lock = threading.Lock()

    def callback(self, signum, frame):
        """SIGALRM signal handler.

        This raises a Timeout exception in a separate thread.
        """
        with self._lock:
            if not self._raised:
                self._raised = True
                t = threading.Thread(target=self.raise_exception)
                t.start()

