import select
import socket
import sys
import time
import traceback
import urllib
import urlparse

from . import __version__
from . import common
from . import config
from . import controller
from . import core
from . import daemon
from . import eventloop
from . import log
from . import lru_cache
from . import manager
from . import proxy
from . import resolver
from . import utils
from . import version


class TCPRelay(object):
    def __init__(self, config, dns_resolver, is_local, stat_callback=None, port_password=None, pre_resolve=None):
        self._config = config
        if is_local:
            self._listen_addr = config.local_address
            self._listen_port = config.local_port
        else:
            self._listen_addr = config.server
            self._listen_port = config.server_port
