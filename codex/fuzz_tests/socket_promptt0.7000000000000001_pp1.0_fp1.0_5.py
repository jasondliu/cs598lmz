import socket
# Test socket.if_indextoname.


class If_indextonameTest(unittest.TestCase):
    def testIt(self):
        try:
            name = socket.if_indextoname(1)
            self.assertEqual(name, 'lo')
        except OSError as e:
            if e.errno == errno.EPERM:
                self.skipTest('requires CAP_NET_ADMIN')
            else:
                raise


if __name__ == '__main__':
    unittest.main()
