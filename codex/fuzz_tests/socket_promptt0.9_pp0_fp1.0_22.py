import socket
# Test socket.if_indextoname
import sys
from test import support

from socket import \
    AF_BLUETOOTH, \
    AF_INET, \
    AF_INET6, \
    AF_UNSPEC, \
    inet_pton
from socket import has_ipv6, if_nameindex, if_nametoindex, if_nametoindex as iname_to_index
from socket import SOL_TCP, SOL_SOCKET, SO_ERROR

try:
    import if_addr
except ImportError:
    inet_ntop = None
else:
    inet_ntop = if_addr.inet_ntop

    def pretty_print_ifaddr(*args):
        args = iter(args)
        while True:
            try:
                family = next(args)
            except StopIteration:
                return
            flags = next(args)
            data = next(args)
            addr_strings = []
            while True:
                try:
                    addr = next(args)
                except StopIteration:
                    break
                mask = next(args)
