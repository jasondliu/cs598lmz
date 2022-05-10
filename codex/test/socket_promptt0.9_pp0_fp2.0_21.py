import socket
# Test socket.if_indextoname()
# Sample usage:
#
# >>> if_indextoname(socket.if_nametoindex('lo')) == 'lo'
# True

import unittest

def if_indextoname(idx):
    try:
        return socket.if_indextoname(idx)
    except OSError:
        pass
    except AttributeError:
        raise unittest.SkipTest("if_indextoname() not available")
    return None

class InterfaceNamesTests(unittest.TestCase):
    def test_interface_names(self):
        n = if_indextoname(1)
        self.assertIsInstance(n, str)
        self.assertTrue(n)
        # The loopback interface is always named 'lo0' on OSX.
        if platform.system() != "Darwin":
            self.assertEqual(if_indextoname(socket.if_nametoindex('lo')), 'lo')

