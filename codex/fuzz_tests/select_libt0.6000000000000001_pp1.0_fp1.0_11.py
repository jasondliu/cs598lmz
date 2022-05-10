import select
import errno
import socket
import threading

from uuid import uuid1
from collections import defaultdict

from circus import logger
from circus.util import (DEFAULT_ENDPOINT_MULTICAST,
                         DEFAULT_ENDPOINT_SUB, DEFAULT_ENDPOINT_PUB,
                         DEFAULT_ENDPOINT_STATS, DEFAULT_ENDPOINT_DEALER,
                         DEFAULT_ENDPOINT_ROUTER, DEFAULT_ENDPOINT_REP,
                         DEFAULT_ENDPOINT_REQ, DEFAULT_ENDPOINT_PUSH,
                         DEFAULT_ENDPOINT_PULL, DEFAULT_ENDPOINT_PIPE,
                         DEFAULT_ENDPOINT_STREAM)
from circus.sockets import CircusSocket
from circus.sockets import CircusSockets
from circus.stream import Stream
from circus.pidfile import Pidfile
from circus.py3compat import string_types


class BaseWatcher(object):
    """Base class for watchers.

   
