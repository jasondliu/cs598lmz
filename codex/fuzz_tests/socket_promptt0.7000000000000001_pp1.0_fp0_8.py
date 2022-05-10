import socket
# Test socket.if_indextoname()
socket.if_indextoname(1)
# END SKIP
"""

def test_socket_if_indextoname(self):
    import socket
    try:
        socket.if_indextoname(1)
    except AttributeError:
        raise self.skipTest("requires socket.if_indextoname")
"""

# SKIPME: This test is currently not run on Windows.
# it's possible that this is a known failure on Windows,
# but I can't find any other tests that skip it.

def test_socket_ntop(self):
    import socket
    try:
        socket.inet_ntop(socket.AF_INET, '\x7f\x00\x00\x01')
    except AttributeError:
        raise self.skipTest("requires socket.inet_ntop")

    self.assertRaises(ValueError, socket.inet_ntop,
                      socket.AF_INET, '\x00' * 5)
    self.assertRaises(ValueError, socket.inet_ntop,
