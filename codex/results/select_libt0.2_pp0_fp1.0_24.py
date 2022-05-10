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
from . import errors
from . import log
from . import utils
from . import x11
from . import xauth

# pylint: disable=too-many-lines

# pylint: disable=too-many-instance-attributes
class SSHClient(object):
    """
    SSH client class.
    """

    def __init__(self, hostname, username, password, port=22, key_filename=None,
                 timeout=None, allow_agent=True, look_for_keys=True,
                 compress=False, sock=None, gss_auth=False,
                 gss_kex=False, gss_deleg_creds=True, gss_host=None,
                 banner_timeout=None, auth_timeout=None,
                 gss_trust_dns=True, passphrase=None,
                 disable_known_hosts=False,
                 host_key
