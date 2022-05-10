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
    def __init__(self, hostname, username, password=None, key_filename=None,
                 timeout=None, port=22, allow_agent=True, look_for_keys=True,
                 compress=False, sock=None, gss_auth=False, gss_kex=False,
                 gss_deleg_creds=True, gss_host=None, banner_timeout=None,
                 auth_timeout=None, gss_trust_dns=True, passphrase=None,
                 disabled_algorithms=None, preferred_auth=None,
                 host_key_policy=None):
        """
        Initialize and connect to the remote host.

        :param str hostname: The remote hostname to connect to.
        :param
