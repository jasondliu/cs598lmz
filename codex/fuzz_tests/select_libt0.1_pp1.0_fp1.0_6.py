import select
import socket
import sys
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
    bind_socket_and_listen_with_backlog_and_accept,
    bind_socket_and_listen_with_backlog_and_accept_and_close,
    bind_socket_and_listen_with_backlog_and_accept_and_close_and_accept,
    bind_socket_and_listen_with_backlog_and_accept_and_close_and_accept_and_close,
    bind_socket_and_listen_with_backlog_and_accept_and_close_and_accept_and_close_and_accept,
    bind_socket_and_listen_with_backlog_and_accept_and_close_
