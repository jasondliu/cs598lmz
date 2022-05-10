import select
import threading
import time
import traceback

import paramiko
import scp

from . import base
from . import config
from . import connection
from . import exceptions
from . import log
from . import utils

LOG = log.get_logger(__name__)

# Define a global variable for the default timeout.
TIMEOUT = config.get_config().getint('ssh', 'timeout')

# Define a global variable for the default port.
DEFAULT_PORT = config.get_config().getint('ssh', 'port')

# Define a global variable for the default user name.
DEFAULT_USERNAME = config.get_config().get('ssh', 'username')


class SSHClient(object):
    """
    This class is a wrapper around the paramiko.SSHClient class. It has
    methods that make it easy to run commands and get their output, as well
    as methods for copying files to/from the remote host.
    """

