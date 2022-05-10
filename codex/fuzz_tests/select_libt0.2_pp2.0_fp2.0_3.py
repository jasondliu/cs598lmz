import selectors
import socket
import types

import pytest

from . import utils
from .utils import (
    assert_raises_os_error,
    assert_raises_socket_error,
    assert_raises_socket_gaierror,
    assert_raises_socket_timeout,
    bind_socket,
    bind_socket_and_listen,
    bind_unix_socket,
    bind_unix_socket_and_listen,
    close_socket,
    close_unix_socket,
    create_connection,
    create_server,
    create_unix_connection,
    create_unix_server,
    find_unused_port,
    get_socket_error,
    get_socket_error_args,
    get_socket_error_errno,
    get_socket_error_strerror,
    get_socket_error_winerror,
    get_socket_error_filename,
    get_socket_error_filename2,
    get_socket_error_str,
    get_socket_error
