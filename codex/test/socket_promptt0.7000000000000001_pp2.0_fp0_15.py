import socket
# Test socket.if_indextoname()
import test.support
import unittest
import uuid

import dns.exception
import dns.name
import dns.inet
import dns.reversename
import dns.zone

class ZoneTestCase(unittest.TestCase):

    def setUp(self):
        self.zone = dns.zone.from_text(text, 'example.', relativize=False)

    def test_from_xfr(self):
        if not dns.query.xfr:
            return
        z = dns.zone.from_xfr(dns.query.xfr('192.0.2.1', 'example.'))
        self.assertEqual(self.zone, z)

