import socket
# Test socket.if_indextoname()
#
# This function is not supported by the current version of python on
# the target. It is supported by Python 3.4.1, and this test should
# be enabled when that version is used on the target.

if_indextoname = socket.if_indextoname

class IfIndexToNameTest(unittest.TestCase):

    def test_if_indextoname(self):
        '''
        This test is expected to fail because if_indextoname is not
        supported on the target.
        '''
        self.assertNotEqual(if_indextoname(0), 'lo')

if __name__ == "__main__":
    unittest.main()
