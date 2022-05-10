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
