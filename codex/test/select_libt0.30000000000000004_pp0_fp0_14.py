import select
import socket
import sys
import threading
import time
import traceback

from . import _common
from . import _errors
from . import _util
from . import _winapi

if sys.platform == 'win32':
    from . import _winapi_pipe_connection
else:
    from . import _posix_pipe_connection

__all__ = [
    'PipeListener',
    'PipeClient',
]


class PipeListener(object):
    """A listener for pipe connections.

    This class is thread-safe.
    """

    def __init__(self, pipe_name, backlog=1):
        """Create a new pipe listener.

        Args:
            pipe_name (str): The name of the pipe to listen on.
            backlog (int): The maximum number of connections to queue.
        """
        self._pipe_name = pipe_name
