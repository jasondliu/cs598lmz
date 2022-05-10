import select
import socket
import sys
import threading
import time
import traceback

import paramiko

from . import common
from . import compat
from . import transport


class SSHClientTransport(transport.SSHClientTransport):
    """
    A paramiko-based SSH client transport.
    """
    def __init__(self, hostname, port, username, password, private_key,
                 *,
                 known_hosts=None,
                 event_handler=None,
                 connect_timeout=None,
                 connect_attempts=None,
                 connect_interval=None,
                 connect_backoff=None,
                 connect_backoff_max=None,
                 connect_keepalive=None,
                 connect_keepalive_interval=None,
                 connect_keepalive_type=None,
                 connect_banner_timeout=None,
                 connect_default_banner=None,
                 connect_default_banner_str=None,
                 connect_default_banner_bytes=None,
                 connect_default_banner_unic
