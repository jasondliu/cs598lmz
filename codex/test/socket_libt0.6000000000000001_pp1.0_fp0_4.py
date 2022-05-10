import socket
import sys
import time

from cStringIO import StringIO
from . import __version__


class _Base(object):
    """Base class for both IP and UNIX connections."""
    def __init__(self, host, port, max_retries, timeout):
        self.host = host
        self.port = port
        self.max_retries = max_retries
        self.timeout = timeout

    def _log_error(self, msg):
        sys.stderr.write('%s\n' % msg)

    def _log_debug(self, msg):
        sys.stdout.write('%s\n' % msg)

    def _send_command(self, cmd, *args):
        """Send a command to the server."""
        args = [str(a) for a in args]
        s = '%s %s\r\n' % (cmd, ' '.join(args))
        self._log_debug(s[:-2])
        self.sock.sendall(s)

