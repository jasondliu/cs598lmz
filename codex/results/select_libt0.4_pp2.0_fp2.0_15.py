import select
import socket
import sys
import threading
import time
import traceback
import tty
import termios

from . import util
from . import errors
from . import constants
from . import __version__

log = logging.getLogger(__name__)


class SSHClient(object):
    """
    An SSH Client.

    This class wraps `paramiko.SSHClient`.

    :param str hostname:
        The server to connect to.

    :param str username:
        The username to authenticate as.

    :param str password: (optional)
        Used for password authentication.

    :param str key_filename: (optional)
        The filename, or list of filenames, of optional private key(s) and/or
        certificates to try for authentication.

    :param int port: (optional)
        The SSH port to connect to. Defaults to 22.

    :param bool allow_agent: (optional)
        Set to False to disable connecting to the SSH agent.

    :param bool look_for_keys: (optional)
        Set to False to disable searching for
