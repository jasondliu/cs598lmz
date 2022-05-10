import select
import socket
import sys
import threading
import time

import pytest

from . import util
from .util import (
    assert_raises_os_error,
    assert_raises_socket_error,
    assert_raises_socket_gaierror,
    assert_raises_socket_timeout,
    bind_socket,
    bind_socket_and_listen,
    bind_socket_and_listen_with_backlog,
    bind_unix_socket_and_listen,
    bind_unix_socket_and_listen_with_backlog,
    check_socket_timeout,
    check_socket_timeout_with_timeout,
    check_socket_timeout_with_timeout_0,
    check_socket_timeout_with_timeout_none,
    check_socket_timeout_with_timeout_valueerror,
    check_socket_timeout_with_timeout_typeerror,
    check_socket_timeout_with_timeout_overflowerror,
    check_socket_timeout_with_timeout_ioerror,
    check_
