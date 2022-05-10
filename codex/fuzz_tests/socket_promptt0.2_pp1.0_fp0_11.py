import socket
# Test socket.if_indextoname()

import unittest
import sys
import os
import errno
import array
import select
import time
import struct
import subprocess

from test import test_support

HOST = test_support.HOST

def if_indextoname(index):
    try:
        return socket.if_indextoname(index)
    except socket.error, msg:
        if msg.args[0] == errno.EINVAL:
            return None
        raise

def if_nametoindex(name):
    try:
        return socket.if_nametoindex(name)
    except socket.error, msg:
        if msg.args[0] == errno.EINVAL:
            return None
        raise

class NetworkInterfaceTests(unittest.TestCase):

    def test_if_name(self):
        # Make sure gethostbyname() works
        name = socket.gethostbyaddr(HOST)[0]
        self.assertTrue(name)

        # Get the interface associated with the host
        try:
            host
