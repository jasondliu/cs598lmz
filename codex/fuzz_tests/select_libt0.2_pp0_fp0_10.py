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
    bind_unix_socket,
    bind_unix_socket_already_bound,
    bind_unix_socket_unavailable,
    check_socket_timeout,
    check_timeout,
    find_unused_port,
    HOST,
    IPV6_ENABLED,
    PORT,
    skip_if_no_ipv6,
    skip_unless_symlink,
    TESTFN,
    unlink,
    wait_for_threads,
)
from .test_socket import (
    create_connection,
    create_server,
    create_unix_server,
    find_ready_matching_sockets,
    get_open_port,
    open_urlresource,
    open_urlresource_localnet,
    open_urlresource_unreachable,
    open_urlresource
