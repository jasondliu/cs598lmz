import select
import socket
import sys
import threading
import time
import traceback
import urllib
import urlparse
import uuid

import pybonjour

from . import exceptions
from . import utils
from . import version

__all__ = ['Service']

_logger = logging.getLogger(__name__)


class Service(object):
    """A service that can be discovered via Bonjour.

    :param str name: name of the service
    :param str type: type of the service
    :param int port: port on which the service is running
    :param str host: host on which the service is running
    :param dict txt: custom TXT record
    :param bool register: whether to register the service or not
    :param bool allow_remote_connections: whether to allow remote connections
        to the service
    :param int timeout: timeout for the service registration
    :param callable register_callback: callback to call when the service is
        registered
    :param callable unregister_callback: callback to call when the service is
        unregistered
    """
