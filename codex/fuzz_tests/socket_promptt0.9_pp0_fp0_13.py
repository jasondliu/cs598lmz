import socket
# Test socket.if_indextoname.
import unittest

SIOCGIFNAME = 0x8910

@unittest.skipUnless(hasattr(socket, 'if_indextoname'),
                     'test needs socket.if_indextoname()')
class IfindexTest(unittest.TestCase):
    def testNames(self):
        ifs = socket.if_names()
        self.assertIn('lo', ifs)
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            for ifname in ifs:
                index = socket.if_nameindex()[ifname]
                self.assertEqual(ifname, s.if_indextoname(index))


if __name__ == '__main__':
    unittest.main()
