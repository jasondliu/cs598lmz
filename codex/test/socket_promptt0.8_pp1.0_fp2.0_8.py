import socket
# Test socket.if_indextoname()
import test.test_support
import unittest

if hasattr(socket, 'if_indextoname'):
    class InterfaceUtilityTest(unittest.TestCase):

        def test_if_indextoname(self):
            index = socket.if_nametoindex('lo')
            name = socket.if_indextoname(index)
            self.assertNotEqual(name, '')


def test_main():
    test.test_support.run_unittest(InterfaceUtilityTest)


if __name__ == '__main__':
    test_main()
