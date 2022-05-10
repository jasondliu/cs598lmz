import socket
# Test socket.if_indextoname support.
#
# Socket module helper for socket(2).
def if_indextoname(index):
    arpa_inet = socket.AF_INET
    try:
        f = getattr(socket, 'if_indextoname', None)
    except AttributeError:
        pass
    else:
        if f is not None:
            return f(index)
    return socket.if_nametoindex(socket.if_indextoname(index))


from time import time
import threading
from socket import socket, AF_INET, SOCK_DGRAM, IPPROTO_UDP, IPPROTO_IP, IP_ADD_MEMBERSHIP

from conftest import IPV6_ENABLED
from common import TestSkipped, find_free_port, verify_ipv6_address, bind_socket, \
    bind_ports


class BaseUDPIPv6SocketTests(BaseIPv6SocketTests):
    def setUp(self):
        if not IPV6_ENABLED:
            raise TestSk
