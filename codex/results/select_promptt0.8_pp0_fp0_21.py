import select
# Test select.select() and select.poll() function.
import socket
import time
import os
import sys
import unittest


def get_scratch_addr():
    bind_test_socket = socket.socket()
    # The socket will be bound on an arbitrary free port.
    bind_test_socket.bind(('', 0))
    if sys.platform in ('linux', 'freebsd', 'netbsd', 'openbsd'):
        # SO_REUSEADDR only applies to IPv4 addresses on many Unix systems
        # (including Linux, FreeBSD, and OpenBSD)
        bind_test_socket.setsockopt(socket.IPPROTO_IP, socket.SO_REUSEADDR, 1)
    bind_test_socket.listen(1)
    scratch_addr = bind_test_socket.getsockname()
    bind_test_socket.close()
    return scratch_addr


class select_thread(threading.Thread):
    def __init__(self, fd_list, timeout, request_event, response_event):
        threading.Thread.__init__
