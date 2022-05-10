import socket
# Test socket.if_indextoname()

try:
    import ifaddr
except ImportError:
    raise unittest.SkipTest("ifaddr module required")

import sysconfig
import netifaces
import os

if sysconfig.get_config_var('HAVE_IF_INDEXTONAME'):
    def if_indextoname(index):
        return socket.if_indextoname(index)
else:
    def if_indextoname(index):
        return None

class IfaddrTests(unittest.TestCase):
    def test_get_adapters(self):
        adapters = ifaddr.get_adapters()
        self.assertNotEqual(len(adapters), 0)
        for adapter in adapters:
            self.assertTrue(adapter.nice_name)
            self.assertTrue(adapter.name)
            self.assertTrue(adapter.friendly_name)
            self.assertTrue(adapter.ips)
        self.assertEqual(len(adapters), len(ifaddr.get_adapters()))

