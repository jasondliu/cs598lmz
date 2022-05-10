import select
import sys
import time

import pytest

from . import util
from .util import (
    assert_raises_os_error,
    assert_raises_regex,
    assert_raises_regex_match,
    bind_socket_and_listen,
    bind_unix_socket_and_listen,
    check_socket_connected,
    check_socket_closed,
    check_socket_open,
    check_socket_timeout,
    check_socket_unconnected,
    close_socket,
    create_connection,
    create_connection_for_url,
    create_server_and_client,
    create_unix_server_and_client,
    get_errno,
    get_free_port,
    get_socket_error,
    get_socket_timeout,
    get_unix_socket_path,
    ignore_resource_warnings,
    make_socket,
    make_socket_with_timeout,
    open_url,
    open_url_with_retry,
    os_
