import socket
# Test socket.if_indextoname()
from test import support

from test.test_support import TESTFN

class IfIndexToNameTests(unittest.TestCase):

    def setUp(self):
        self.name = socket.if_indextoname(1)

    def tearDown(self):
        support.unlink(TESTFN)

    def test_basic(self):
        self.assertTrue(isinstance(self.name, str))
        self.assertTrue(self.name)

    def test_name_error(self):
        self.assertRaises(socket.error, socket.if_indextoname, 0)

    def test_name_type_error(self):
        self.assertRaises(TypeError, socket.if_indextoname, None)


def test_main():
    tests = [IfIndexToNameTests]
    support.run_unittest(*tests)


if __name__ == "__main__":
    test_main()
