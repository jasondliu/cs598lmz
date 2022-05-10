import socket

from unittest import TestCase
from unittest import mock
from unittest.mock import Mock

from ocflib.infra.net import reverse_dns
from ocflib.infra.net import validate_ip


class TestReverseDNS(TestCase):

    def test_localhost(self):
        self.assertEqual(reverse_dns('127.0.0.1'), 'localhost')

    def test_dne(self):
        self.assertEqual(reverse_dns('127.0.0.2'), '127.0.0.2')

    def test_fake(self):
        self.assertEqual(reverse_dns('127.0.0.3'), '127.0.0.3')

    @mock.patch('socket.gethostbyaddr', return_value=('foo.bar.com', (), ()))
    def test_resolves(self, mock_gethostbyaddr):
        self.assertEqual(reverse_dns('127.0.0.4'), 'foo.bar.
