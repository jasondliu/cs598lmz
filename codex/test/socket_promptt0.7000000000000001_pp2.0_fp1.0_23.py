import socket
# Test socket.if_indextoname

import os.path
import subprocess
from collections import namedtuple
from contextlib import closing
from functools import wraps

import pytest

from support import socket_helper as sh

import socket

def if_indextoname(index):
    try:
        return socket.if_indextoname(index)
    except OSError:
        return None

@pytest.mark.skipif(not hasattr(socket, 'if_indextoname'),
                    reason='if_indextoname not supported')
@sh.skip_unless_bind_unix_socket
def test_if_indextoname():
    iface_idx = sh.get_interface_index_with_ip(sh.IPV4_HOST)
    assert socket.if_indextoname(iface_idx) == sh.get_interface_name(sh.IPV4_HOST)
    assert if_indextoname(iface_idx + 1) is None

