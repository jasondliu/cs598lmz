import socket
# Test socket.if_indextoname() in Python distribution
# across various platforms
# Tested with Python 3.2


class BadInterfaceNameException(Exception):
    pass


class TestCases(unittest.TestCase):
    def test_null(self):
        self.assertEqual(socket.if_indextoname(0), '')

    def test_loopback(self):
        # First, I'd like to make sure that socket.if_indextoname() works
        # as expected on Linux.
        self.assertEqual(socket.if_indextoname(1),
                'lo')
        # Then, we use loopback as a testbed for the rest of the tests.
        # If loopback is not the first interface, neither
        # socket.if_indextoname() nor socket.if_indextoname() are
        # reliable functions.
        # If it returns b'' or None, socket.if_indextoname() is not reliable.
        self.check_reliable(1)

    def check_reliable(self, test):
        self.assertNotE
