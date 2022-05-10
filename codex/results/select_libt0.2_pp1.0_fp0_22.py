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

    def __init__(self, host, port=22, username=None, password=None,
                 key_filename=None, timeout=10, connect_timeout=10,
                 banner_timeout=10, proxy_host=None, proxy_port=None,
                 proxy_username=None, proxy_password=None,
                 proxy_key_filename=None, proxy_timeout=10,
                 proxy_connect_timeout=10, proxy_banner_timeout=10,
                 proxy_sock=None, proxy_transport=None,
                 proxy_allow_agent=True, proxy_look_for_keys=True,
                 proxy_compress=False, proxy_g
