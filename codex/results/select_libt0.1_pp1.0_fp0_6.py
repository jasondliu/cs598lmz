import select
import socket
import sys
import threading
import time
import traceback

import paramiko

from . import common
from . import config
from . import constants
from . import exceptions
from . import log
from . import utils

LOG = log.getLogger(__name__)

# The default SSH port
DEFAULT_SSH_PORT = 22

# The default timeout for SSH connections
DEFAULT_SSH_TIMEOUT = 10

# The default timeout for SSH commands
DEFAULT_SSH_COMMAND_TIMEOUT = 60

# The default timeout for SSH connections
DEFAULT_SSH_CONNECT_TIMEOUT = 10

# The default timeout for SSH connections
DEFAULT_SSH_CONNECT_RETRIES = 3

# The default timeout for SSH connections
DEFAULT_SSH_CONNECT_RETRY_DELAY = 5

# The default timeout for SSH connections
DEFAULT_SSH_CONNECT_RETRY_BACKOFF = 2

# The default timeout for SSH connections
DEFAULT_SSH_CONNECT_RETRY_JITTER =
