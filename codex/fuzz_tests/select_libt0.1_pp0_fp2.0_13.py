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
    bind_socket,
    bind_unix_socket,
    check_socket_connected,
    check_socket_not_connected,
    check_socket_timeout,
    check_socket_timeout_with_timeout,
    check_socket_timeout_with_timeout_value,
    check_socket_timeout_with_timeout_zero,
    check_socket_timeout_with_timeout_none,
    check_socket_timeout_with_timeout_negative,
    check_socket_timeout_with_timeout_non_numeric,
    check_socket_timeout_with_timeout_non_numeric_type,
    check_socket_timeout_with_timeout_non_numeric_value,
    check_socket_timeout_with_timeout_non_numeric_type_value,
    check_socket_timeout_with_timeout_non_numeric_type_
