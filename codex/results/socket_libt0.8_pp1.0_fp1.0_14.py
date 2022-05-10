import socket
import threading
import time
import traceback
from collections import deque
from socket import SOCK_DGRAM
from typing import Any, Deque, List, Optional

import gnupg
import paramiko
from paramiko.dsskey import DSSKey
from paramiko.ecdsakey import ECDSAKey
from paramiko.ed25519key import Ed25519Key
from paramiko.kex_gex import KexGex
from paramiko.kex_group1 import KexGroup1
from paramiko.kex_group14 import KexGroup14
from paramiko.pkey import PKey
from paramiko.rsakey import RSAKey
from paramiko.ssh_exception import SSHException

from . import enums
from . import py2util
from . import py3util
from . import util
from .common import Common
from .client_exception import AuthenticationException, ParamikoException

if py2util.PY2:
    from . import RSAKey as _RSAKey


logger = logging.getLogger(__name__)


class Policy(
