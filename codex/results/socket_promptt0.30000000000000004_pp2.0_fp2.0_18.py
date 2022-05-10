import socket
# Test socket.if_indextoname()

class IfIndexToNameTest(unittest.TestCase):

    def test_if_indextoname(self):
        if_index = socket.if_nametoindex('lo')
        if_name = socket.if_indextoname(if_index)
        self.assertEqual(if_name, 'lo')

    def test_if_indextoname_invalid_index(self):
        self.assertRaises(OSError, socket.if_indextoname, 0)

    def test_if_indextoname_non_string_index(self):
        self.assertRaises(TypeError, socket.if_indextoname, None)

class IfNameToIndexTest(unittest.TestCase):

    def test_if_nametoindex(self):
        if_index = socket.if_nametoindex('lo')
        self.assertEqual(if_index, 1)

    def test_if_nametoindex_invalid_name(self):
        self.assertRaises(OSError, socket.if
