import select
import signal
import sys
import time

from . import daemon
from . import log
from . import utils
from . import version

_log = log.get_logger(__name__)


def _get_config_dir():
    """
    Return the configuration directory.
    """
    return os.path.join(os.path.expanduser('~'), '.config', 'dnssec-trigger')


def _get_config_file():
    """
    Return the configuration file.
    """
    return os.path.join(_get_config_dir(), 'dnssec-trigger.conf')


def _get_control_socket_path():
    """
    Return the path of the control socket.
    """
    return os.path.join(_get_config_dir(), 'control.sock')


def _get_run_dir():
    """
    Return the runtime directory.
    """
    return os.path.join(os.path.expanduser('~'), '.cache', 'dnssec-trigger')


