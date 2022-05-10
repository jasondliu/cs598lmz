import socket
# Test socket.if_indextoname - convert a socket address family default to name
import test.test_support, unittest


class interfaceTest(unittest.TestCase):
    def testIfIndextoname(self):
        # Checks if socket.if_indextoname works for at least AF_INET family
        indextoname = socket.if_indextoname(socket.AF_INET, 1)
        self.assertNotEqual(indextoname, None)
        self.addCleanup(setattr, socket, 'if_indextoname',
                        socket.if_indextoname)

def test_main(verbose=None):
    test.test_support.run_unittest(interfaceTest)

if __name__ == '__main__':
    test_main()
