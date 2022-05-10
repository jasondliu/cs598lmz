import select
import socket
import sys
import time
import traceback

import pytest

from . import util
from .util import (
    assert_raises_os_error,
    assert_raises_regex,
    bind_unix_socket,
    bind_unix_socket_alg,
    bind_unix_socket_cloexec,
    bind_unix_socket_prefer_ipv6,
    check_socket_family,
    check_socket_timeout,
    check_socket_timeout_default,
    check_socket_timeout_exc,
    check_socket_timeout_exc_errno,
    check_socket_timeout_exc_nonblocking,
    check_socket_timeout_exc_nonblocking_errno,
    check_socket_timeout_exc_nonblocking_noerrno,
    check_socket_timeout_exc_nonblocking_noerrno_msg,
    check_socket_timeout_exc_nonblocking_noerrno_msg_nonascii,
    check_socket_timeout_exc_nonblocking_noerrno_
