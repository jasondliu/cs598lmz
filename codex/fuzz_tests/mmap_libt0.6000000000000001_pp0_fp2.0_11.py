import mmap
import os
import re
import socket
import struct
import sys
import time
from cStringIO import StringIO

from collections import namedtuple
from contextlib import contextmanager

from . import errors
from .compat import (
    PY2,
    PY3,
    abc,
    is_callable,
    is_integer,
    is_string,
    iteritems,
    long_type,
    next,
    num_types,
    string_types,
    text_type,
    xrange,
    zip,
)
from .constants import (
    ALL_FLAGS,
    ALL_PORT_TYPES,
    CMD_GET,
    CMD_SET,
    CMD_SET_WITH_ATTRS,
    CMD_SET_WITH_ATTRS_AND_GET_OLD,
    DEFAULT_CMD_TIMEOUT,
    DEFAULT_HEARTBEAT_TIMEOUT,
    DEFAULT_HEARTBEAT_INTERVAL,
    DEFAULT_MAX_CONNECTIONS_PER
