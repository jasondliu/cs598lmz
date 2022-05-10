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
    bind_unix_socket_truncate,
    bind_unix_socket_unlink_on_close,
    bind_unix_socket_unlink_on_close_alg,
    bind_unix_socket_unlink_on_close_cloexec,
    bind_unix_socket_unlink_on_close_prefer_ipv6,
    bind_unix_socket_unlink_on_close_truncate,
    bind_unix_socket_unlink_on_close_unlink_on_close,
    bind_unix_socket_unlink_on_close_unlink_on_close
