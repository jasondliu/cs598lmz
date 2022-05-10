import socket
import sys
import threading
import time
import traceback

import paramiko

from . import util

LOG = logging.getLogger(__name__)


class SSHClient(object):
    """
    A wrapper around paramiko.SSHClient that provides a more Pythonic API.
    """
