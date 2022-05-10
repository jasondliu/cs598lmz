import select
import socket
import sys
import threading
import time
import traceback

import pytest

from . import util
from .util import (
    get_open_port,
    get_unused_port,
    get_unused_tcp_port,
    get_unused_udp_port,
    get_unused_local_port,
    get_unused_local_tcp_port,
    get_unused_local_udp_port,
    get_ipv6_addrinfo,
)

try:
    import ssl
except ImportError:
    ssl = None

if sys.platform == "win32":
    from .util import (
        bind_socket_to_random_port,
        bind_unix_socket,
        bind_unix_socket_mswindows,
        bind_unix_socket_mswindows_stat,
        bind_unix_socket_mswindows_tmpfile,
        bind_unix_socket_mswindows_tmpnam,
        bind_unix_socket_mswindows_tmp
