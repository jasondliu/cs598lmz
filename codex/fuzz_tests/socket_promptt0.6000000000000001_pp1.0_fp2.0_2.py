import socket
# Test socket.if_indextoname()

import unittest
import socket
import sys
import os

from test.support import (
    run_unittest, TESTFN, run_with_locale, check_warnings,
    unix_socket_path, reap_children, find_unused_port,
    bind_port, requires_mac_ver, requires_linux_version, requires_android_api
)

HOST = 'localhost'
MSG = b'Michael Gilfix was here\u2119\u0115\u212f\u2131'

try:
    socket.IPPROTO_IPV6
except AttributeError:
    raise unittest.SkipTest("IPv6 is not supported")

try:
    socket.IPV6_V6ONLY
except AttributeError:
    raise unittest.SkipTest("IPV6_V6ONLY is not supported")

has_ipv6 = socket.has_ipv6

@unittest.skipUnless(has_ipv6, 'IPv6 not supported')
class BaseIPv6T
