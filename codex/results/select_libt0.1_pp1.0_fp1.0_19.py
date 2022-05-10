import select
import socket
import sys
import threading
import time

import pytest

from . import util
from .util import (
    assert_raises_os_error,
    assert_raises_regex,
    assert_raises_socket_error,
    bind_socket,
    bind_socket_and_listen,
    bind_socket_and_listen_with_backlog,
    bind_unix_socket,
    bind_unix_socket_and_listen,
    bind_unix_socket_and_listen_with_backlog,
    check_socket_timeout,
    check_timeout,
    check_timeout_with_sleep,
    check_timeout_with_sleep_and_read,
    check_timeout_with_sleep_and_write,
    check_timeout_with_sleep_and_write_into,
    check_timeout_with_sleep_and_writev,
    check_timeout_with_sleep_and_writev_into,
    check_timeout_with_write,
    check_timeout_with_
