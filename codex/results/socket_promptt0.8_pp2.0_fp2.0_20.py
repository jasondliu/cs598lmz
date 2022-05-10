import socket
# Test socket.if_indextoname and socket.if_nametoindex on Linux.
# The implementation of these two functions can be found in
# Linux inet/devinet.c
import sys
import pytest

from test import support
import unittest
from unittest import mock
from functools import reduce

class InterfaceTest(unittest.TestCase):

    def test_if_indextoname(self):
        if_indextoname = socket.if_indextoname
        if_nametoindex = socket.if_nametoindex
        with support.suppress_warnings() as sup:
            sup.filter(DeprecationWarning, "IF_NAMESIZE is deprecated")
            self.assertEqual(set(if_indextoname(if_nametoindex(i))
                                 for i in if_indextoname(0, b'\0'*256)
                                 if i),
                             set(if_indextoname(0, b'\0'*256)))
            for i in range(0, 256):
                self.assertEqual(if
