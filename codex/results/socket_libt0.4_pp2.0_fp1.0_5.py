import socket
import sys
import threading
import time
import traceback

import paramiko

from . import constants
from . import exceptions
from . import util

__all__ = ['SSHClient']

_logger = logging.getLogger(__name__)


class SSHClient(object):
    """
    A high-level representation of a session with an SSH server.  This class
    wraps `.Transport` and `.Channel` to take care of most aspects of
    authentication and executing commands and transferring files.

    This class is intended to make SSHv2 connections.  If you want to make
    SSHv1 connections, see `.SSHClient`.

    This class depends on the `paramiko` module, and will not function if
    it is not installed.

    :param str hostname: the server to connect to
    :param int port: the server port to connect to
    :param str username: the username to authenticate as (defaults to the
        current local username)
    :param str password: a password to use for authentication or for
        unlocking a private key
    :param str
