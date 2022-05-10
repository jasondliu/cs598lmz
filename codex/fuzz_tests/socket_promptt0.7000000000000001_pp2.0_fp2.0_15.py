import socket
# Test socket.if_indextoname()
# Test socket.if_nametoindex()
import os
import sys
import string
import time
import re

if sys.version_info >= (3, 0):
    import urllib.request as urllib2
else:
    import urllib

interface_index = 0
interface_name = ""
if socket.has_ipv6:
    try:
        interface_index = socket.if_nametoindex('lo')
        interface_name = socket.if_indextoname(interface_index)
    except Exception:
        pass

def test_has_ipv6():
    if sys.platform not in ('win32', 'android'):
        assert socket.has_ipv6 is True

def test_socket_inet_pton():
    if socket.has_ipv6:
        socket.inet_pton(socket.AF_INET6, '::1')
        socket.inet_pton(socket.AF_INET6, '::')
        assertRaisesErrno(socket.error, socket.inet_pton, socket.AF
