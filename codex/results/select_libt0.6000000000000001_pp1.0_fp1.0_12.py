import select
import sys
import time

from collections import deque

try:
    from queue import Queue
except ImportError:
    from Queue import Queue

import paramiko

from . import __version__
from . import config
from . import constants
from . import errors
from . import logger
from . import messages
from . import terminal
from . import utils


log = logger.get_logger(__name__)


class SSHClient(paramiko.SSHClient):
    """
    Wrapper around paramiko.SSHClient
    """

    def __init__(self, *args, **kwargs):
        super(SSHClient, self).__init__(*args, **kwargs)
        self.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    def connect(self, hostname, port=22, username=None, password=None,
                pkey=None, key_filename=None, timeout=None,
                allow_agent=True, look_for_keys=True,
                compress=False, sock=None, gss
