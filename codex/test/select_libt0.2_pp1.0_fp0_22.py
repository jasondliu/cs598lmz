import select
import socket
import sys
import threading
import time
import traceback

import paramiko

from . import config
from . import logger
from . import util

log = logger.get_logger(__name__)


class SSHClient(paramiko.SSHClient):
    """
    A subclass of paramiko.SSHClient that adds some convenience methods
    for running commands and transferring files.
    """
