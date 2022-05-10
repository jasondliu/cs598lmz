import select
import socket
import sys
import threading
import time

import paramiko

from . import config

logger = logging.getLogger(__name__)

# we check host keys by default if we know about them
KNOWN_HOSTS = paramiko.util.load_host_keys(os.path.expanduser('~/.ssh/known_hosts'))

# windows does not have termios...
try:
    import termios
    import tty
    has_termios = True
except ImportError:
    has_termios = False


def _read_ssh_config(hostname):
    """
    Reads SSH configuration for the given hostname.

    :param str hostname: Hostname to read configuration for.
    :return: SSH configuration for the given hostname.
    :rtype: paramiko.SSHConfig
    """
    config_file = os.path.expanduser('~/.ssh/config')
    if os.path.exists(config_file):
        with open(config_file) as f:
            return paramiko
