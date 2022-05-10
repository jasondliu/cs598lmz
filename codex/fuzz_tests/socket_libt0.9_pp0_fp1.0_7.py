import socket
import sys
import termios
import tty

from . import settings
from .pkg_mgmt.native import pkg_config
from . import util
from .util import Logger

# Note: OS support is defined using the loose semantics
# used in Python 3.3, plus extended to 2.6 and 2.7.
#
# TODO: remove 2.6+ when we rock python 2.6 support

__OS_SUPPORT = {
    'cygwin',
    'darwin',
    'linux2'
}

__ARCH_SUPPORT = {
    'i386',
    'i686',
    'x86_64'
}

def get_os_version():
    """
    Get the current 64-bit compatible host OS name (e.g., darwin, linux2).
    The detected OS must be supported by Munki.

    Returns None if OS is not supported.
    """
    sysname, hostname, release, version, machine = os.uname()
    if sysname == "Linux":
        # Python reports "Linux"
