import socket
# Test socket.if_indextoname()

from test.support import find_unused_port
import unittest
from contextlib import closing


class IfIndextonameTestCase(unittest.TestCase):
    def test_if_indextoname(self):
        with closing(socket.socket(socket.AF_INET, socket.SOCK_DGRAM)) as s:
            # Find a free port number.
            port = find_unused_port()
            # Get the interface name of the loopback device.
            ifname = socket.if_indextoname(s.getsockopt(socket.SOL_SOCKET,
                                                        socket.SO_BINDTODEVICE,
                                                        4))
            # Bind the socket to the loopback device.
            # Note that this is only allowed for root.
            s.bind((socket.gethostbyname('localhost'), port, ifname))


def test_main():
    run_unittest(IfIndextonameTestCase)


if __name__ == "__main__":
    test_main()
