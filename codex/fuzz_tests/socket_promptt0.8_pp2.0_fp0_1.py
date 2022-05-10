import socket
# Test socket.if_indextoname()
#
import unittest
from test import support


class If_IndextonameTestCase(unittest.TestCase):
    def test_if_indextoname(self):
        nic_names = socket.if_indextoname(1, 1)
        self.assertEqual(len(nic_names), 1)
        self.assertIsInstance(nic_names, list)
        self.assertIsInstance(nic_names[0], str)


if __name__ == "__main__":
    unittest.main()
