import socket
# Test socket.if_indextoname to convert an interface
# index to its name.
import os
import test.support


class InterfaceTest(unittest.TestCase):
    def test_empty_length(self):
        with self.assertRaises(ValueError):
            socket.if_indextoname(0, '')

    def test_null(self):
        name = socket.if_indextoname(0, '\0')

        # We accept both '' and None here, because the C code is
        # inconsistent.
        self.assertIn(name, ('', None))

    @unittest.skipUnless(os.name == 'nt', 'Windows-specific test')
    @test.support.reap_threads
    def test_windows_name_to_index(self):
        # Test name_to_index on Windows.
        network_interfaces = socket.if_nameindex()

        if len(network_interfaces) == 0:
            self.skipTest("no network interfaces found")

        for index, name in network_interfaces:
            self.assertEqual(index,
